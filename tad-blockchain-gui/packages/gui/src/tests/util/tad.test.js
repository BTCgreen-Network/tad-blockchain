const tad = require('../../util/tad');

describe('tad', () => {
  it('converts number mojo to tad', () => {
    const result = tad.mojo_to_tad(1000000);

    expect(result).toBe(0.000001);
  });
  it('converts string mojo to tad', () => {
    const result = tad.mojo_to_tad('1000000');

    expect(result).toBe(0.000001);
  });
  it('converts number mojo to tad string', () => {
    const result = tad.mojo_to_tad_string(1000000);

    expect(result).toBe('0.000001');
  });
  it('converts string mojo to tad string', () => {
    const result = tad.mojo_to_tad_string('1000000');

    expect(result).toBe('0.000001');
  });
  it('converts number tad to mojo', () => {
    const result = tad.tad_to_mojo(0.000001);

    expect(result).toBe(1000000);
  });
  it('converts string tad to mojo', () => {
    const result = tad.tad_to_mojo('0.000001');

    expect(result).toBe(1000000);
  });
  it('converts number mojo to colouredcoin', () => {
    const result = tad.mojo_to_colouredcoin(1000000);

    expect(result).toBe(1000);
  });
  it('converts string mojo to colouredcoin', () => {
    const result = tad.mojo_to_colouredcoin('1000000');

    expect(result).toBe(1000);
  });
  it('converts number mojo to colouredcoin string', () => {
    const result = tad.mojo_to_colouredcoin_string(1000000);

    expect(result).toBe('1,000');
  });
  it('converts string mojo to colouredcoin string', () => {
    const result = tad.mojo_to_colouredcoin_string('1000000');

    expect(result).toBe('1,000');
  });
  it('converts number colouredcoin to mojo', () => {
    const result = tad.colouredcoin_to_mojo(1000);

    expect(result).toBe(1000000);
  });
  it('converts string colouredcoin to mojo', () => {
    const result = tad.colouredcoin_to_mojo('1000');

    expect(result).toBe(1000000);
  });
});
