import { describe, it, expect } from 'vitest';
import { add, isPositive } from '../src/math.js';

describe('add', () => {
  it('returns correct sum', () => expect(add(2, 3)).toBe(5));
  it('handles negative operands', () => expect(add(-2, -3)).toBe(-5));
  it('boundary at zero', () => expect(add(0, 0)).toBe(0));
  it('result is a number', () => expect(typeof add(1, 2)).toBe('number'));
});

describe('isPositive', () => {
  it('positive', () => expect(isPositive(1)).toBe(true));
  it('negative', () => expect(isPositive(-1)).toBe(false));
  it('zero is not positive', () => expect(isPositive(0)).toBe(false));
});
