<template>
    <div class="fraction">

        <div class="numerator">
            <div v-if="!isInput">
                {{ numerator }}
            </div>
            <div v-else>                
                <input placeholder="?" class="input" type="text" :value=numerator  @input="$emit('update:numerator', parseInt($event.target.value))">
            </div>

        </div>
        <div class="denominator">
            <div v-if="!isInput">
                {{ denominator }}
            </div>
            <div v-else>                
                <input placeholder="?" class="input" type="text" :value=denominator @input="$emit('update:denominator', parseInt($event.target.value))">
            </div>
        </div>
    </div>
</template>

<script>
export default {
    mounted() {
        console.log(this.isInput);
    },
    props: {
        numerator: {
            type: Number,
            required: false,
            default: ""
        },
        denominator: {
            type: Number,
            required: false,
            default: ""
        },
        isInput: {
            type: Boolean,
            required: false,
            default: false,
        }
    },
    methods: {
        formatInputDenominator($event) {                        
            this.$emit(`update:denominator`, parseInt($event.target.value))
        },
        formatInputNumerator($event) {                        
            this.$emit(`update:numerator`, parseInt($event.target.value))
        }
    }
}
</script>


<style>
.fraction {
    position: relative;
    width: 1.7em;
    font-size: 2em;
}

.numerator {
    border-bottom: 2px solid black;
    text-align: center;
}

.denominator {
    width: 1.7em;
    text-align: center;
}

.input{
    border: 0.5px blue solid;
    width: 1.7em;
    height: 1.7em;
    text-align: center;
}
</style>