import { defineStore } from 'pinia'

export const useUserStore = defineStore('$user', {
    state: () => {
        return { name: ''}
    },    
    actions: {
        resetUserName() {
            this.name = '';
        },
    },
})