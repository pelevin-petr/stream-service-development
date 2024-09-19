import type { ErrorObject } from '@vuelidate/core'


export const useValidationErrors = <T extends Record<keyof T, string>>(errors: ErrorObject[]): Record<keyof T, string> => {
  return errors.reduce((acc, value) => {
    return { ...acc, [value.$property]: value.$message }
  }, {} as Record<keyof T, string>)
}

export const useValidationErrorsForFile = (errors: ErrorObject[]): Record<string, string> => {
  const result: Record<string, string> = {}

  errors.forEach(error => {
    if (error.$property === 'file') {
      result['file'] = <string>error.$message
    }
  })

  return result
}
