---
title: Banach and Hilbert spaces
order: 10
topics:
- Hilbert Spaces
- Norms
---

# Banach and Hilbert spaces

A Banach space is complete for its norm; a Hilbert space is complete for a norm coming from an inner product.
Completeness is what makes Cauchy approximation arguments land inside the space.
The inner product adds orthogonality, projections, Fourier coefficients, and the identification of continuous linear functionals with vectors.
Thus every Hilbert space is Banach, but the extra geometry is the part used in proofs.

For an orthonormal basis $(e_n)$, Bessel gives $\sum |\langle x,e_n\rangle|^2\le\|x\|^2$ and Parseval upgrades this to equality when the system is complete.
Riesz--Fischer is the converse existence statement behind the coefficient description, while Riesz representation says every continuous functional on a Hilbert space is $x\mapsto\langle x,y\rangle$ for a unique $y$ (with the convention for which variable is linear fixed once and for all).

[[PR-L35O7]]

[[PR-WS6NT]]

[[PR-KTZZ5]]

[[T-5AALA]]

[[FT-NFMJW]]

[[T-LDCZB]]

[[FF-UT5GL]] [[FT-OR6TO]]

[[T-J3AN3]]

::: {.remark title="What the inner product buys"}
A norm coming from an inner product satisfies the parallelogram law, and that is exactly the condition -- so a problem asking whether a given space is a Hilbert space is asking you to test the parallelogram law, usually on two well-chosen functions.

On any measure space containing two disjoint measurable sets of positive finite measure, $L^p$ satisfies the parallelogram law only for $p=2$: normalized indicators of the two sets already give the counterexample for $p\neq2$ (and for $p=\infty$).  Thus in the standard nondegenerate $L^p$ settings, Hilbert-space arguments using orthogonal projection and inner products are special to $L^2$.
:::
