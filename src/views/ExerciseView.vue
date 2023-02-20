<script setup>
import Wizard from '@/components/icons/Wizard.vue';
import Fraction from '@/components/Fraction.vue';
import { useUserStore } from '@/stores/user';
import axios from 'axios';
import { ref, computed } from 'vue'

const $user = useUserStore();

console.log($user);

const api = axios.create({
    baseURL: 'http://localhost:5004/',
    withCredentials: true
});


const numerator1 = ref(1);
const numerator2 = ref(1);
const denominator1 = ref(1);
const denominator2 = ref(1);



function requestExercice() {
    let res = api.get('/exercicio').then(resp => {
        console.log(resp);
        numerator1.value = resp.data['n1'];
        numerator2.value = resp.data['n2'];
        denominator1.value = resp.data['d1'];
        denominator2.value = resp.data['d2'];
    }).catch(error => {
        console.log(error);
    });

}
requestExercice();


const canEditAnswer = ref(true);
const canEditMiddleStep = ref(true);

const showMiddleStep = ref(false);
const showAnswer = ref(true);
const showSimplification = ref(false);


const ansnumerator = ref();
const ansdenominator = ref();
function checkAnswer() {

    if (showAnswer.value == true && !passou_resposta)
        checkUnsimplifiedAnswer();
    if (!showAnswer.value)
        checkMiddleStep();
    if (passou_resposta)
        checkSimplifiedAnswer();
}


const ms_n1 = ref();
const ms_n2 = ref();
const ms_d1 = ref();
const ms_d2 = ref();
let passou_mmc = false;
let passou_resposta = false;
function checkMiddleStep() {

    const params = {
        "n1": numerator1.value,
        "d1": denominator1.value,
        "n2": numerator2.value,
        "d2": denominator2.value,
        "rn1": ms_n1.value,
        "rd1": ms_d1.value,
        "rn2": ms_n2.value,
        "rd2": ms_d2.value
    }

    console.log(params)

    let res = api.post('/passo_intermediario', params).then(resp => {
        let mensagem = resp.data['message'];
        // let resultado = resp.data['resultado'];        
        window.alert(mensagem);
        if (mensagem == 'correto') {
            canEditMiddleStep.value = false;
            showAnswer.value = true;
            passou_mmc = true;
        }
    }).catch(error => {
        console.log(error);
    });
    console.log(res);
}

function checkUnsimplifiedAnswer() {
    console.log(ansnumerator.value);
    const params = {
        'n1': numerator1.value,
        'n2': numerator2.value,
        'd1': denominator1.value,
        'd2': denominator2.value,
        'rn': ansnumerator.value,
        'rd': ansdenominator.value
    }

    console.log(params)

    let res = api.post('/resposta_simples', params).then(resp => {
        let mensagem = resp.data['message'];
        let resultado = resp.data['resultado'];
        // window.alert(resultado);
        window.alert(mensagem);
        if (mensagem == 'errado' && !passou_mmc) {
            showMiddleStep.value = true;
            showAnswer.value = false;
            ansnumerator.value = 0
            ansdenominator.value = 0
        }
        if (mensagem == 'correto') {

            if (resultado[0] != ansnumerator.value &&
                resultado[1] != ansdenominator.value) {

                window.alert("precisa simplificar");

                passou_resposta = true;
                showSimplification.value = true;
                canEditAnswer.value = false;
                canEditSimplification.value = true;
            } else {
                fimExercicio();
            }
        }


    }).catch(error => {
        console.log(error);
    });
    console.log(res);
}

const s_ansnumerator = ref();
const s_ansdenominator = ref();
function checkSimplifiedAnswer() {
    console.log(ansnumerator.value);
    const params = {
        'n1': numerator1.value,
        'n2': numerator2.value,
        'd1': denominator1.value,
        'd2': denominator2.value,
        'rn': s_ansnumerator.value,
        'rd': s_ansdenominator.value
    }

    console.log(params)

    let res = api.post('/resposta_simples', params).then(resp => {
        let mensagem = resp.data['message'];
        let resultado = resp.data['resultado'];
        // window.alert(resultado);
        window.alert(mensagem);

        if (mensagem == 'correto' &&
            resultado[0] != s_ansnumerator.value &&
            resultado[1] != s_ansdenominator.value) {

            window.alert("precisa simplificar");
        } else {
            fimExercicio();
        }

    }).catch(error => {
        console.log(error);
    });
    console.log(res);
}

function fimExercicio() {
    $user.increaseProgress();
    window.alert("fim do exercício");

}
// const stepOneEnabled = computed(() => {
//     return !(answerEnabled.value);
// });


</script>

<script>
export default {
    data() {
        return {
            test: "Hello world"
        }
    }
}
</script>

<template>
    <main>
        <v-container class="container">
            
            <div class="panel-login" align="center">
                <div class="progress-bar">
                    <v-progress-linear
                    v-model="$user.progress"
                    height="10"
                    :buffer-value="$user.totalExercises"
                    color="blue"
                    ></v-progress-linear>
                </div>

                <h1 class="text-center font-weight-light">{{ $user.name }}, você sabe resolver esse exercício?</h1>



                <div class="exercise"> <!-- Apresentação do exercício-->
                    <Fraction :numerator=numerator1 :denominator=denominator1 class="mr-3" />

                    <span class="operator mr-3">+</span>

                    <Fraction class="mr-3" :numerator=numerator2 :denominator=denominator2 />

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

                    <RouterLink to="/">
                        <v-btn class="mt-5 bg-red btn">
                            Desistir
                        </v-btn>
                    </RouterLink>
                </div>
            </div>

        </v-container>
    </main>
</template>


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
</style>
