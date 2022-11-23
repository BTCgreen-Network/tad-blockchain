import { useLocalStorage } from '@tad/api-react';

export default function useEnableDataLayerService() {
  return useLocalStorage<boolean>('enableDataLayerService', false);
}
