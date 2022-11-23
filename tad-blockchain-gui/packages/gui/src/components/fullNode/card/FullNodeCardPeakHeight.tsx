import { useGetBlockchainStateQuery } from '@tad/api-react';
import { FormatLargeNumber, CardSimple } from '@tad/core';
import { Trans } from '@lingui/macro';
import React from 'react';

export default function FullNodeCardPeakHeight() {
  const { data, isLoading, error } = useGetBlockchainStateQuery();
  const value = data?.peak?.height ?? 0;

  return (
    <CardSimple
      loading={isLoading}
      valueColor="textPrimary"
      title={<Trans>Peak Height</Trans>}
      value={<FormatLargeNumber value={value} />}
      error={error}
    />
  );
}
