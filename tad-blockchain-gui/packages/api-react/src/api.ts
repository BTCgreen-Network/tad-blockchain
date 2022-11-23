import { createApi } from '@reduxjs/toolkit/query/react';

import tadLazyBaseQuery from './tadLazyBaseQuery';

export const baseQuery = tadLazyBaseQuery({});

export default createApi({
  reducerPath: 'tadApi',
  baseQuery,
  endpoints: () => ({}),
});
