import React, { useMemo } from 'react';
import { Trans } from '@lingui/macro';
import { useCurrencyCode, mojoToTadLocaleString, CardSimple } from '@tad/core';
import { useGetFarmedAmountQuery } from '@tad/api-react';

export default function FarmCardTotalTadFarmed() {
  const currencyCode = useCurrencyCode();
  const { data, isLoading, error } = useGetFarmedAmountQuery();

  const farmedAmount = data?.farmedAmount;

  const totalTadFarmed = useMemo(() => {
    if (farmedAmount !== undefined) {
      return (
        <>
          {mojoToTadLocaleString(farmedAmount)}
          &nbsp;
          {currencyCode}
        </>
      );
    }
  }, [farmedAmount]);

  return (
    <CardSimple
      title={<Trans>Total Tad Farmed</Trans>}
      value={totalTadFarmed}
      loading={isLoading}
      error={error}
    />
  );
}
