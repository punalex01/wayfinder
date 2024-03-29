import { IUser } from './User';

export interface IPayment {
  name: string;
  date: Date;
  lender: IUser; // User
  isReturned: boolean;
  total: number;
  lendeeAmounts: LendeeAmount[];
  uuid: string;
}

export interface LendeeAmount {
  user: IUser; // User
  amount: number;
  isReturned: boolean;
}

export interface IPaymentOwed {
  name: string;
  total: number;
  paymentUUID: string;
}

export interface IIndividualPayment {
  name: string;
  amount: number;
  isIndividual: boolean;
  date: Date;
}
