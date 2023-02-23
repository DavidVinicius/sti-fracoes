<style scoped>
.btn {
    width: 150px;
}

.progress-bar {
    margin-bottom: 50px;
}

.container {
    width: 100vw;
    align-items: center;
}

.panel-login {
    width: 50vw;
    margin: 0 auto !important;
}

.exercise {
    display: flex;
    flex-flow: row;
    justify-content: center;
    align-items: center;
}

.operator {
    font-size: 2rem;
}

.help {
    margin-top: 50px;
    font-size: 1rem;
}
</style>

<template>
    <main>
        <v-container class="container">
            
            <div class="panel-login" align="center">
                <div class="progress-bar">
                    <v-progress-linear
                    v-model="$userStore.progress"
                    height="10"
                    :buffer-value="$userStore.totalExercises"
                    color="blue"
                    ></v-progress-linear>
                </div>

                <h1 class="text-center font-weight-light">{{ $userStore.name }}, você sabe resolver esse exercício? </h1>

                <div class="exercise"> <!-- Apresentação do exercício-->
                    <Fraction :numerator="numerator1" :denominator="denominator1" class="mr-3" />

                    <span class="operator mr-3">+</span>

                    <Fraction class="mr-3" :numerator="numerator2" :denominator="denominator2" />

                    <span class="operator mr-3">=</span>

                </div>



                <div class="exercise" v-if=showMiddleStep> <!-- Passo Intermediário (MMC)-->
                    <Fraction :is-input="canEditMiddleStep" class="mr-3" v-model:numerator=ms_n1
                        v-model:denominator=ms_d1 />

                    <span class="operator mr-3">+</span>

                    <Fraction :is-input="canEditMiddleStep" class="mr-3" v-model:numerator=ms_n2
                        v-model:denominator=ms_d2 />

                    <span class="operator mr-3">=</span>

                </div>



                <div class="exercise" v-if=showAnswer> <!-- RESPOSTA ANTES SIMPLIFICAÇÃO-->

                    <Fraction class="mr-3" :is-input=canEditAnswer v-model:numerator=ansnumerator
                        v-model:denominator=ansdenominator />

                    <span class="operator mr-3" v-if="showSimplification">=</span>
                </div>



                <div class="exercise" v-if=showSimplification> <!-- SIMPLIFICAÇÃO-->
                    <Fraction :is-input=true class="mr-3" v-model:numerator=s_ansnumerator
                        v-model:denominator=s_ansdenominator />


                </div>

                <div style="display:flex; justify-content: center; flex-flow: column;">
                    <div>
                        <v-btn @click="checkAnswer()" class="mt-5 bg-blue btn">
                            Responder
                        </v-btn>
                    </div>
                    <div style="display:flex; justify-content: center; flex-flow: column;">
                        <div>
                            <v-btn @click="tryToSkip()" class="mt-5 bg-red btn">
                                Pular
                            </v-btn>
                        </div>
                    </div>

                    <!-- <RouterLink to="/">
                                <v-btn class="mt-5 bg-red">
                                    Desistir
                                </v-btn>
                            </RouterLink> -->
                </div>

                <div class="help">
                    <a href="help/index.htm" target="_blank">Está precisando de ajuda com o conteúdo?</a>
                </div>
            </div>

        </v-container>
    </main>
</template>

<script>
import Fraction from '@/components/Fraction.vue';
import axios from 'axios';
import { mapStores } from 'pinia'
import { useUserStore } from '@/stores/user';
import cookies from '../cookie'


const api = axios.create({
    baseURL: 'http://localhost:5004/',
    withCredentials: true
});

export default {
    mounted() {
        console.log(this.$toast);
        this.requestExercice();
    },
    components: {
        Fraction
    },
    data() {
        return {
            msgTutoria: "",
            passou_mmc: false,
            passou_resposta: false,
            canEditAnswer: true,
            canEditMiddleStep: true,
            canEditSimplification: true,
            showMiddleStep: false,
            showAnswer: true,
            showSimplification: false,

            numerator1: 1,
            numerator2: 1,
            denominator1: 1,
            denominator2: 1,

            ms_n1: null,
            ms_n2: null,
            ms_d1: null,
            ms_d2: null,

            ansnumerator: null,
            ansdenominator: null,

            s_ansnumerator: null,
            s_ansdenominator: null,

            Passos: {                    //Estados para acompanhar se aluno respondeu direto
                INICIO: "INICIO",               //Exercicio está na primeira etapa
                TODAS_ETAPAS: "TODAS_ETAPAS",	//Errou conta direta, fazendo processo longo    
                SIMPLIFICA: "SIMPLIFICA"        //Faltou simplificar
            },
            passo: "INICIO"
        }
    },
    computed: {
        ...mapStores(useUserStore)
    },
    methods: {
        requestExercice() {
            let res = api.get('/exercicio').then(resp => {
                console.log(resp);
                this.numerator1 = resp.data['n1'];
                this.numerator2 = resp.data['n2'];
                this.denominator1 = resp.data['d1'];
                this.denominator2 = resp.data['d2'];
                this.msgTutoria = resp.data['msgTutoria'];
            }).catch(error => {
                console.log(error);
            });
        },
        checkAnswer() {
            

            if (this.showAnswer == true && !this.passou_resposta)
                this.checkUnsimplifiedAnswer();
            this.passo = this.Passos.TODAS_ETAPAS
            if (!this.showAnswer) {
                this.passo = this.Passos.TODAS_ETAPAS
                this.checkMiddleStep();
            }
            if (this.passou_resposta) {
                this.passo = this.Passos.SIMPLIFICA;
                this.checkSimplifiedAnswer();
            }
        },
        checkUnsimplifiedAnswer() {
            console.log(this.ansnumerator);
            if (this.ansdenominator == null || this.ansnumerator == null) {
                this.$toast.error("Preencha a resposta primeiro");
                return;
            }
            

            const params = {
                'n1': this.numerator1,
                'n2': this.numerator2,
                'd1': this.denominator1,
                'd2': this.denominator2,
                'rn': this.ansnumerator,
                'rd': this.ansdenominator,
                'passo': this.passo
            }

            console.log(params)

            let res = api.post('/resposta_simples', params).then(resp => {
                let mensagem = resp.data['message'];
                let resultado = resp.data['resultado'];
                
                this.$toast.info(resp.data['msgTutoria']);

                if (mensagem == 'errado' && !this.passou_mmc) {
                    this.showMiddleStep = true;
                    this.showAnswer = false;
                    this.ansnumerator = 0;
                    this.ansdenominator = 0;
                }

                if (mensagem == 'correto') {

                    if (resultado[0] != this.ansnumerator &&
                        resultado[1] != this.ansdenominator) {

                        this.passou_resposta = true;
                        this.showSimplification = true;
                        this.canEditAnswer = false;
                        this.canEditSimplification = true;
                    } else if (resultado[0] == this.ansnumerator && resultado[1] == this.ansdenominator) {
                        this.fimExercicio();
                    }
                }


            }).catch(error => {
                console.log(error);
            });
            console.log(res);
        },
        checkSimplifiedAnswer() {
            console.log(this.ansnumerator);
            const params = {
                'n1': this.numerator1,
                'n2': this.numerator2,
                'd1': this.denominator1,
                'd2': this.denominator2,
                'rn': this.s_ansnumerator,
                'rd': this.s_ansdenominator,
                'passo': this.passo
            }

            console.log(params)

            let res = api.post('/resposta_simples', params).then(resp => {
                let mensagem = resp.data['message'];
                let resultado = resp.data['resultado'];
                this.$toast.info(resp.data['msgTutoria']);

                if (mensagem == 'correto' &&
                    resultado[0] != this.s_ansnumerator &&
                    resultado[1] != this.s_ansdenominator) {
                    this.$toast.info("Ainda é necessário simplificar");

                } else if (mensagem == 'correto' &&
                    resultado[0] == this.s_ansnumerator &&
                    resultado[1] == this.s_ansdenominator) {
                    
                    this.fimExercicio();
                }

            }).catch(error => {
                console.log(error);
            });
            console.log(res);
        },
        checkMiddleStep() {

            if (this.ms_d1 == null || this.ms_d2 == null || this.ms_n1 == null || this.ms_n2 == null) {
                this.$toast.error("Preencha a resposta primeiro");
                return;
            }

            const params = {
                "n1": this.numerator1,
                "d1": this.denominator1,
                "n2": this.numerator2,
                "d2": this.denominator2,
                "rn1": this.ms_n1,
                "rd1": this.ms_d1,
                "rn2": this.ms_n2,
                "rd2": this.ms_d2,
                'passo': this.passo
            }

            console.log(params)

            let res = api.post('/passo_intermediario', params).then(resp => {
                let mensagem = resp.data['message'];
                // let resultado = resp.data['resultado'];        
                

                //window.alert(mensagem);
                if (mensagem == 'correto') {
                    this.canEditMiddleStep = false;
                    this.showAnswer = true;
                    this.passou_mmc = true;
                    this.$toast.show("Você acertou a etapa intermediária!");
                } else {
                    this.$toast.info(resp.data['msgTutoria']);
                }
            }).catch(error => {
                console.log(error);
            });
            console.log(res);
        },
        tryToSkip() {
            // window.alert("skip");
            if (!this.showMiddleStep) {
                // passo = Passos.TODAS_ETAPAS; 
                this.$toast.info("Tente resolver o problema em etapas");
                this.showMiddleStep = true;
                this.showAnswer = false;
                this.ansnumerator = null;
                this.ansdenominator = null;
                return;
            }

            let res = api.post('/pularExercicio').then(resp => {
                this.$toast.show("Pulando exercício");
                this.fimExercicio(false);
            }).catch(error => {
                console.log(error);
            });

        },
        fimExercicio(accert = true) {
            if (accert) {
                this.$userStore.increaseProgress();
                this.$toast.success("Continue assim!");
            }

            if (this.$userStore.progress == 100) {
                this.$router.push('/final');
            }
            
            this.requestExercice();
            this.ansnumerator = null;
            this.ansdenominator = null;
            this.ms_d1 = null;
            this.ms_d2 = null;
            this.ms_n1 = null;
            this.ms_n2 = null;
            this.showMiddleStep = false;
            this.showAnswer = true;
            this.showSimplification = false;
            this.passou_mmc = false;
            this.passou_resposta = false;
            this.canEditAnswer = true;
            this.canEditMiddleStep = true;
            this.canEditSimplification = true;
        }
    }
}
</script>


