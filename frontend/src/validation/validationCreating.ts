import { computed, ref } from 'vue'
import { helpers, required } from '@vuelidate/validators'
import { useVuelidate } from '@vuelidate/core'

import type { IFormCreate } from '@/validation/helpers'
import { FORM_REQUIRED_FIELD } from '@/validation/helpers'
import { useValidationErrors } from '@/validation/useValidationErrors'



const formCreate = ref<IFormCreate>({
  title: '',
  description: ''
})

const rulesCreate = {
  title: {
    required: helpers.withMessage(FORM_REQUIRED_FIELD, required)
  },
  description: {}

}

export const $vCreate = useVuelidate(rulesCreate, formCreate)

export const errorsCreate = computed(() => useValidationErrors<IFormCreate>($vCreate.value.$errors))
