export interface IFormCreate {
  title: string;
  description: string;
}
export interface IFormDelete {
  deleteId: string;
}

export const FORM_REQUIRED_FIELD: string = 'Это поле обязательно для заполнения';