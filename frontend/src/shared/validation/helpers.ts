  export interface IFormCreate {
    title: string;
    description: string;
    file: File | undefined;
  }
  export const FORM_REQUIRED_FIELD: string = 'Это поле обязательно для заполнения';