interface StreamDescription {
  carNumber: string;
  whenIncluded: Date;
  //geolocation: ???  //just idea, im don't know
  streamer: string;  //or author or car number
  smallDescription?: string;
  city: string;   //or other specific information
}

export interface Stream {
  readonly id: number;
  link: string;
  description: StreamDescription;
  included: boolean;  //we need to get info about streams(included or not)
}