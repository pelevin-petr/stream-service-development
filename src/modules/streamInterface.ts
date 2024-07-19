interface StreamDescription {
  name: string;
  whenIncluded: Date;
  //geolocation: ???  //just idea, im don't know
  strimer: string;  //or author or car number
  smallDescription?: string;
}

export interface Stream {
  readonly id: number;
  link: string;
  description: StreamDescription;
  city: string;   //or other specific information
  included: boolean;  //we need to get info about streams(included or not)
}