import { FC, useState } from 'react';
import { PaymentsModule } from '../PaymentsModule';
import { AddPaymentModal } from './AddPaymentModal';

export const GroupFinancials: FC = () => {
  const [isAddPaymentModalOpen, setAddPaymentModalOpen] = useState(false);

  return (
    <>
      <div className='flex flex-col h-full w-full'>
        <div className='h-16 w-full px-3 flex items-center border-b-2 border-gray-600 py-3 justify-between'>
          <div className='text-3xl h-10'>Group Payments</div>
          <div className='space-x-3 '>
            <button
              onClick={() => setAddPaymentModalOpen(true)}
              className='h-10 w-32 border rounded-md border-eggplant/20 bg-eggplant/50 hover:bg-eggplant text-white'
            >
              Add Payment
            </button>
            <AddPaymentModal
              isAddPaymentModalOpen={isAddPaymentModalOpen}
              setAddPaymentModalOpen={setAddPaymentModalOpen}
            />
          </div>
        </div>
        <PaymentsModule />
      </div>
    </>
  );
};