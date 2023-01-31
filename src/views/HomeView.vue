<script setup>
  import Wizard from '@/components/icons/Wizard.vue';
  import { useUserStore } from '@/stores/user';
  const $user = useUserStore();
</script>

<template>
  <main>
        <v-container class="container">
          <div class="panel-login" align="center">
            <h1 class="text-center font-weight-light">Bem-vindo ao matemágika</h1>
            <Wizard />
        
            <div>
              <v-text-field label="Digite seu nome" v-model="$user.name" hide-details="auto"></v-text-field>
            </div>
        
            <RouterLink to="/about">
              <v-btn class="mt-5 bg-blue">
                Iniciar
              </v-btn>
            </RouterLink>
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
</style>
