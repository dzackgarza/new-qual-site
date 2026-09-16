---
schema: qual/card@1
id: PR-ULJAJ
kind: proposition
title: Properties of the Blaschke factors $\psi_a$
classification:
  areas:
  - complex-analysis
  topics:
  - Blaschke Factors
  - Biholomorphisms
relations: []
review: draft
---

::: {.proposition}
For $a\in\DD$ let $\psi_a(z)=\frac{a-z}{1-\bar az}$ be the [[D-MFPYG|Blaschke factor]]. Then:

- $\psi_a\in\Aut(\DD)$, and $\psi_a$ maps the unit circle $S^1$ onto itself;

- $\psi_a(0)=a$ and $\psi_a(a)=0$;

- $\psi_a\circ\psi_a=\id_\DD$, so $\psi_a^{-1}=\psi_a$;

- $\psi_a'(z)=\frac{\abs{a}^2-1}{(1-\bar az)^2}$;

- $\psi_a(\lambda z)=\lambda\,\psi_{\bar\lambda a}(z)$ for every $\lambda\in\CC$ with $\abs\lambda=1$.
:::

::: {.proof}
The denominator $1-\bar az$ is nonzero for $\abs{z}\le1$, since $\abs{\bar az}<1$.
For $\abs{z}=1$, $\abs{1-\bar az}=\abs{\bar z-\bar a}=\abs{a-z}$, so $\abs{\psi_a(z)}=1$.
By the maximum modulus principle $\abs{\psi_a}<1$ on $\DD$ ($\psi_a$ is nonconstant because $\abs a<1$).
The values at $0$ and $a$ are immediate.
A direct computation gives
$$
\psi_a(\psi_a(z))=\frac{a(1-\bar az)-(a-z)}{(1-\bar az)-\bar a(a-z)}=\frac{z(1-\abs a^2)}{1-\abs a^2}=z,
$$
so $\psi_a$ is a bijection of $\DD$ equal to its own inverse, hence in $\Aut(\DD)$, and likewise a bijection of $S^1$.
By the quotient rule,
$$
\psi_a'(z)=\frac{-(1-\bar az)+\bar a(a-z)}{(1-\bar az)^2}=\frac{\abs a^2-1}{(1-\bar az)^2}.
$$
Finally, for $\abs\lambda=1$, $\lambda\bar\lambda=1$ gives
$$
\lambda\,\psi_{\bar\lambda a}(z)=\lambda\,\frac{\bar\lambda a-z}{1-\lambda\bar az}=\frac{a-\lambda z}{1-\bar a\lambda z}=\psi_a(\lambda z).
$$
:::
