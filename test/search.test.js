const { aofsr } = require('./search.js');

test('aofsr should return true when phraseMode is true', () => {
    const result = aofsr({
        phraseMode: true
    });
    expect(result).toBe(true);
});