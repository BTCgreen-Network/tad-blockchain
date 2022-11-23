import { ServiceName } from '@tad/api';
import { useService } from '@tad/api-react';
import { CardSimple } from '@tad/core';
import { Trans } from '@lingui/macro';
import React from 'react';

export default function FullNodeCardConnectionStatus() {
  const { isRunning, isLoading, error } = useService(ServiceName.FULL_NODE);

  return (
    <CardSimple
      loading={isLoading}
      valueColor={isRunning ? 'primary' : 'textPrimary'}
      title={<Trans>Connection Status</Trans>}
      value={isRunning ? <Trans>Connected</Trans> : <Trans>Not connected</Trans>}
      error={error}
    />
  );
}
