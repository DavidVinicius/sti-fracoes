import { defineStore } from 'pinia'

export const useUserStore = defineStore('$user', {
    state: () => {
        return { 
            name: '',
            totalExercises: 10,
            progress: 0,
            accerts: 0,
            level: "",
            errors: 0,
            actualExercise: {
                trials: 0,
            }
        }
    },   
    getters: {
        userData(state) {
            return {
                progress: state.progress,
                accerts: state.progress,
                errors: state.errors
            };
        }
    },  
    actions: {
        resetUserName() {
            this.name = '';
        },
        increaseProgress() {
            this.accerts += 1;
            this.progress += 10;
        },
        registerError() {
            this.errors += 1;
            this.actualExercise.trials += 1;
        }
    },
})