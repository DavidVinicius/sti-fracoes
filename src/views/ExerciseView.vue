<script setup>
    import Wizard from '@/components/icons/Wizard.vue';
    import Fraction from '@/components/Fraction.vue';
    import { useUserStore } from '@/stores/user';
    const $user = useUserStore();
</script>

<template>
    <main>
        <v-container class="container">
            <div class="panel-login" align="center">
                <h1 class="text-center font-weight-light">{{ $user.name }}, você sabe resolver esse exercício?</h1>
                    
                <div class="exercise">
                    <Fraction :numerator="3"  :denominator="8" class="mr-3"/>
                    
                    <span class="operator mr-3">+</span>
                    
                    <Fraction class="mr-3" :numerator="5"  :denominator="2"/>
                    
                    <span class="operator mr-3">=</span>
                    
                    <Fraction :is-input="true" class="mr-3" />
                </div>
    
                <div style="display:flex; justify-content: center; flex-flow: column;">
                    <RouterLink to="/about">
                        <v-btn class="mt-5 bg-blue">
                            Responder
                        </v-btn>
                    </RouterLink>
                    
                    <RouterLink to="/">
                        <v-btn class="mt-5 bg-red">
                            Desistir
                        </v-btn>
                    </RouterLink>
                </div>
            </div>
    
        </v-container>
    </main>
</template>


<style scoped>
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

.operator{
    font-size: 2rem;
}
</style>
