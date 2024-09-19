// interface StreamDescription {
//   carNumber: string;
//   whenTurnOn: Date;
//   //geolocation: ???  //just idea, im don't know
//   streamer: string;  //or author or car number
//   smallDescription?: string;
//   city: string;   //or other specific information
// }

export interface BaseStream {
  readonly id: string;
  title: string;
  description: string;
}

export interface Stream {
  stream: BaseStream,
  file_url: string
}