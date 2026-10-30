---
schema: qual/card@1
id: P-AGFS15-04
kind: problem
title: Laurent-polynomial maps on the punctured affine line
classification:
  areas: [algebraic-geometry]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the retained Algebraic Geometry FS 15 exam-guidelines PDF dated August 12, 2015.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified extension to the projective line, the unit-group classification of automorphisms of the torus, and the function-field criterion for bijectivity on rational differentials in arbitrary characteristic.
- event: source-checked
  by: claude-opus-5.5
  date: 2026-10-31
  note: Part (b) asks when the extension f-bar is an automorphism (of P^1), not f; statement and solution corrected.
---
::: {.problem}
Let $f\in k[z,z^{-1}]$ be viewed as a morphism
$$
f:\AA^1\setminus\{0\}\longrightarrow\AA^1.
$$

(a) Show that $f$ extends uniquely to a morphism $\overline f:\PP^1\to\PP^1$.

(b) For which $f$ is $\overline f$ an automorphism?

(c) For which $f$ is
$$
\overline f^{\,*}:\Omega_{\PP^1}\longrightarrow\Omega_{\PP^1}
$$
an isomorphism? Here $\Omega_{\PP^1}$ is the $k(\PP^1)$-vector space of rational differentials on $\PP^1$.
:::

::: {.solution}
Write $K=k(z)=k(\PP^1)$.

::: pf

::: {.pf-step #s1}

Every Laurent polynomial extends uniquely to $\PP^1$.

::: pf-proof

A Laurent polynomial $f$ is an element of the rational function field $K=k(z)$. A rational function on the nonsingular complete curve $\PP^1$ determines a morphism to $\PP^1$: at a point where $f$ is finite it has value $[f:1]$, and at a pole it has value $[1:0]$. Thus $f$ extends to a morphism
$$
\overline f:\PP^1\longrightarrow\PP^1.
$$

The punctured affine line is a dense open subset of $\PP^1$. Since $\PP^1$ is separated, two morphisms $\PP^1\to\PP^1$ agreeing on a dense open subset agree everywhere. Hence the extension is unique.

:::

:::

::: {.pf-step #s2}

The extension $\overline f$ is an automorphism of $\PP^1$ exactly for
$$
\boxed{f(z)=az+b\quad\text{or}\quad f(z)=az^{-1}+b,\qquad a\in k^\times,\ b\in k.}
$$

::: pf-proof

The morphism $\overline f:\PP^1\to\PP^1$ is an automorphism exactly when the rational function $f$ has degree $1$, that is, when $k(f)=k(z)$.
A rational function of degree $1$ has exactly one pole, and that pole is simple; a constant has degree $0$.
Since $f\in k[z,z^{-1}]$, its only possible poles are $0$ and $\infty$.
If the pole is $\infty$, then $f$ is a polynomial of degree $1$, so $f(z)=az+b$ with $a\ne0$.
If the pole is $0$, then $f(z)=az^{-1}+b$ with $a\ne0$.
Conversely, each of these has the inverse $w\mapsto(w-b)/a$ or $w\mapsto a/(w-b)$, so $\overline f$ is an automorphism.

:::

:::

::: {.pf-step #s3}

The pullback on rational differentials is an isomorphism exactly for
$$
\boxed{f(z)=az+b\quad\text{or}\quad f(z)=az^{-1}+b,\qquad a\in k^\times,\ b\in k.}
$$

::: pf-proof

The $K$-vector space of rational differentials is one-dimensional:
$$
\Omega_{\PP^1}=K\,dz.
$$
For $h(z)\in K$, pullback by $\overline f$ is
$$
\overline f^{\,*}(h(z)\,dz)
=h(f(z))\,df
=h(f(z))f'(z)\,dz.
$$
Hence its image is
$$
\operatorname{im}(\overline f^{\,*})=f'(z)\,k(f(z))\,dz.
$$
If $f'(z)=0$, the pullback is zero and cannot be an isomorphism. If $f'(z)\ne0$, multiplication by $f'(z)$ is invertible in $K$, so the pullback is surjective exactly when
$$
k(f(z))=k(z).
$$
By step [](#s2){.pf-ref}, this holds exactly for the listed functions, and for them $f'$ is $a$ or $-az^{-2}$, which is nonzero. The pullback is injective in every case with $f'\ne0$, because $K\to K$, $h\mapsto h(f)f'$, is an injective field map followed by multiplication by a unit.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} proves the unique extension, step [](#s2){.pf-ref} classifies when $\overline f$ is an automorphism, and step [](#s3){.pf-ref} classifies when pullback on rational differentials is an isomorphism.

:::

:::

:::
