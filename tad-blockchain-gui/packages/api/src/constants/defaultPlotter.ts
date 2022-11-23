import defaultsForPlotter from '../utils/defaultsForPlotter';
import optionsForPlotter from '../utils/optionsForPlotter';
import PlotterName from './PlotterName';

export default {
  displayName: 'Tad Proof of Space',
  options: optionsForPlotter(PlotterName.TADPOS),
  defaults: defaultsForPlotter(PlotterName.TADPOS),
  installInfo: { installed: true },
};
