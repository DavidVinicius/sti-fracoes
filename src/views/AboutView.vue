<script setup>
  import Wizard from '@/components/icons/Wizard.vue';
  import { useUserStore } from '@/stores/user';
  const $user = useUserStore();
</script>

<template>
  <div class="about">
    <v-container class="container">
      <div class="panel-login" align="center">
        <h1 class="text-center font-weight-light">Olá, {{ $user.name }}</h1>
        <Wizard />
    
        <div>
          Seja bem-vindo ao Matemágika, um Sistema Tutorial Inteligente (STI) desenvolvido para te ajudar a exercitar e melhorar seus conhecimentos de matemática. Resolva os exercícios em passos, calculando o MMC, ou de uma só vez, caso você já conheça a resposta. Mas atenção, não esqueça de simplicar as frações ao final!
          <br><br>
          E aí, preparado para se tornar o mago da soma de frações?
        </div>
    

        <RouterLink to="/">
          <v-btn class="mt-5 bg-grey mr-2" @click="$user.resetUserName()">
            Voltar
          </v-btn>
        </RouterLink>

        <RouterLink to="/learn">
          <v-btn class="mt-5 bg-blue">
            Próxima etapa
          </v-btn>
        </RouterLink>

        <div class="help">
            <br>
            <a href="help/index.htm" target="_blank">Se precisar de ajuda, clique aqui!</a>
        </div>
      </div>
    
    </v-container>
  </div>
</template>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}

.container {
  width: 100vw;
  align-items: center;
}
</style>
