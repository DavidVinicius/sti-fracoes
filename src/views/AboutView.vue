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
          Lorem ipsum, dolor sit amet consectetur adipisicing elit. Velit fugit amet doloribus nihil accusantium mollitia corporis officiis modi delectus omnis iste, odit voluptate debitis asperiores expedita. Tenetur quam quos at?
          Minus, animi quos. Officia sequi, iusto reiciendis nisi eum aliquid asperiores rem quos voluptatum quis sunt minima dignissimos qui accusamus harum laboriosam, aliquam soluta! Est sapiente ut praesentium a veniam?
          Id iure illum atque voluptatem dignissimos. Accusamus tempora sit mollitia repudiandae nemo. Corrupti earum incidunt porro, reiciendis voluptatem, omnis exercitationem, non illum magnam voluptas rem autem consequatur ab officia modi.
          Nihil illum, nobis fugiat tempora alias maxime labore, aliquam cupiditate porro officiis, similique veniam atque mollitia et incidunt eaque sint eos ab enim hic. Deleniti dolorem veniam odit placeat nemo?
          Minima architecto voluptatum ullam dolores nam ab suscipit voluptatibus fugit maxime porro temporibus adipisci eos autem assumenda a eius veritatis unde consectetur delectus soluta aliquam laborum, reiciendis esse. Nam, quas?
          Rem a maiores natus asperiores, et cum unde eos, iusto necessitatibus animi magnam saepe eaque doloribus minima omnis molestias, nemo iure? Nulla consequuntur totam saepe sapiente asperiores id illo ut.
          Placeat velit facere vero magni, autem architecto tempore nostrum nisi distinctio molestias aspernatur corporis ea optio vitae alias eaque provident minima! Nemo, et ipsam ratione ducimus enim minus omnis qui.
          Ducimus, quasi ad quaerat in porro tempora similique voluptates sit. Autem, inventore neque aspernatur atque aliquam tempore repellendus cumque ex pariatur commodi tempora, provident perferendis, animi culpa libero nihil consequuntur!
          Sapiente beatae itaque, accusamus reiciendis quo nesciunt ipsum amet. Nesciunt neque alias animi cumque explicabo blanditiis quidem beatae, numquam hic repudiandae, tempora eum architecto sed quod laborum autem nostrum minima.
          Accusantium excepturi, quas quam ea mollitia iusto in doloremque delectus sint ratione, illo debitis cumque, labore est? Expedita inventore fugit aliquam alias reiciendis quia, sapiente fugiat veritatis maiores eaque non.
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
