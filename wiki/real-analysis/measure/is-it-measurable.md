---
title: Is it measurable?
order: 0
problems:
  topics:
  - Measure Theory
  - Measurable Functions
---

# Is it measurable?

Measurability is almost never proved from the definition.
It is inherited, and the work is naming which closure property applies.

## The inheritance rules

A function is measurable if it is built from measurable pieces by any of:

- composition with a continuous function on the outside;
- pointwise limits, $\liminf$, $\limsup$, $\sup_n$, $\inf_n$ of a countable family;
- sums, products, quotients with nonvanishing denominator;
- restriction to a measurable set, and gluing countably many such.

Continuous implies Borel measurable, monotone implies Borel measurable, and a.e. equality preserves Lebesgue measurability.
Between them these settle nearly every function a problem produces.

## The order matters

Continuous $\circ$ measurable is measurable; measurable $\circ$ continuous need not be.
This is the standard trap, and the reason is that measurability pulls back measurable sets, so the outer function must be the well-behaved one.

The witness is built from the Cantor function: it maps a null set onto a set of positive measure, so it carries a non-measurable set back to a measurable one.

[[FF-UW3C7]]

[[FE-YOIJM]]

[[PR-Z5VSQ]]

## When the answer is no

Non-measurable sets exist only by choice, so a problem asking for one wants the Vitali construction: quotient $[0,1]$ by $\QQ$, choose a representative from each class, and observe that countably many translates both cover $[0,1]$ and sit inside $[-1,2]$, so its measure can be neither zero nor positive.

Consequences worth having: every set of positive measure contains a non-measurable subset, and Lebesgue measurable is strictly weaker than Borel, since Lebesgue is the completion.

## Exercises

[[P-QZT5B]]

[[P-TZJQI]]
