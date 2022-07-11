import React, { useMemo } from 'react';
import { Trans } from '@lingui/macro';
import { useCurrencyCode, mojoToTadLocaleString, CardSimple, useLocale } from '@tad/core';
import { useGetFarmedAmountQuery } from '@tad/api-react';

export default function FarmCardTotalTadFarmed() {
  const currencyCode = useCurrencyCode();
  const [locale] = useLocale();
  const { data, isLoading, error } = useGetFarmedAmountQuery();

  const farmedAmount = data?.farmedAmount;

  const totalTadFarmed = useMemo(() => {
    if (farmedAmount !== undefined) {
      return (
        <>
          {mojoToTadLocaleString(farmedAmount, locale)}
          &nbsp;
          {currencyCode}
        </>
      );
    }
  }, [farmedAmount, locale, currencyCode]);

  return (
    <CardSimple
      title={<Trans>Total Tad Farmed</Trans>}
      value={totalTadFarmed}
      loading={isLoading}
      error={error}
    />
  );
}
