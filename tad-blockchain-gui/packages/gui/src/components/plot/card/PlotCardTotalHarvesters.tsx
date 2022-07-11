import React from 'react';
import { Trans } from '@lingui/macro';
import { FormatLargeNumber, CardSimple } from '@tad/core';
import { useGetTotalHarvestersSummaryQuery } from '@tad/api-react';

export default function PlotCardTotalHarvesters() {
  const { harvesters, isLoading } = useGetTotalHarvestersSummaryQuery();

  return (
    <CardSimple
      title={<Trans>Total Harvesters</Trans>}
      value={<FormatLargeNumber value={harvesters} />}
      loading={isLoading}
    />
  );
}