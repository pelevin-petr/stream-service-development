import { computed, ref } from 'vue'
import { helpers, required } from '@vuelidate/validators'
import { useVuelidate } from '@vuelidate/core'

import type { IFormCreate } from '@/shared/validation/helpers'
import { FORM_REQUIRED_FIELD } from '@/shared/validation/helpers'
import { useValidationErrors, useValidationErrorsForFile } from '@/shared/validation/useValidationErrors'


const formCreate = ref<IFormCreate>({
  title: '',
  description: '',
  file: undefined
})

const rulesCreate = {
  title: {
    required: helpers.withMessage(FORM_REQUIRED_FIELD, required)
  },
  description: {},
  file: {
    required: helpers.withMessage(FORM_REQUIRED_FIELD, required)
  }

}

export const $vCreate = useVuelidate(rulesCreate, formCreate)

export const errorsCreate =computed(() => ({
  ...useValidationErrorsForFile($vCreate.value.$errors),
  ...useValidationErrors($vCreate.value.$errors)
}))