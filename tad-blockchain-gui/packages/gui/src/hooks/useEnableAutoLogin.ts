import { useLocalStorage } from '@tad/api-react';

export default function useEnableAutoLogin() {
  return useLocalStorage<boolean>('enableAutoLogin', true);
}
