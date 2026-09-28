---
schema: qual/card@1
id: D-DIVAMPLE
kind: definition
title: Ample and very ample divisors
classification:
  areas:
  - algebraic-geometry
  topics:
  - Ample Divisors
  - Very Ample Divisors
  - Linear Systems
relations:
- kind: uses
  target: T-DIVMAPPN
review: draft
prompts:
- What is a very ample divisor?
- What is an ample divisor?
- What is the difference between ample and very ample?
- What is a hyperplane section?
---

::: {.definition title="Very ample"}
Let $X$ be a noetherian scheme over a field $k$, let $D$ be a Cartier divisor, and put $\mcl=\OO_X(D)$.
The divisor $D$ is \dfn{very ample} over $k$ if $\mcl$ is [[D-MODAMPLE|very ample]] over $k$: there is an immersion $\iota:X\to\PP_k^n$ with $\iota^*\OO(1)\cong\mcl$ [@Har10a, Chapter II, §7].
:::

::: {.definition title="Ample"}
On a noetherian scheme $X$, a Cartier divisor $D$ is \dfn{ample} if its associated invertible sheaf $\OO_X(D)$ is [[D-MODAMPLE|ample]] [@Har10a, Chapter II, §7].
:::

::: {.proposition}
If $X$ is of finite type over $k$, then $D$ is ample if and only if $nD$ is very ample over $k$ for some $n>0$ [@Har10a, Theorem II.7.6].
If $X$ is a projective integral variety over an algebraically closed field, then $D$ is very ample if and only if its [[D-DIVLINSYS|complete linear system]] is base-point free and its associated morphism is a closed immersion.
Equivalently, $D$ is linearly equivalent to a hyperplane section under some projective embedding [@Har10a, Chapter II, §7].
:::

::: {.proposition title="Tensor products and finite pullback"}
On a noetherian scheme, the tensor product of an ample invertible sheaf with a globally generated invertible sheaf is ample, as is the tensor product of two ample invertible sheaves.
If $\mcl$ is ample and $\mcm$ is any invertible sheaf, then $\mcm\otimes\mcl^{\otimes n}$ is ample for all sufficiently large $n$ [@Har10a, Exercise II.7.5].
For a finite morphism $f:Y\to X$ of noetherian schemes and an ample invertible sheaf $\mcl$ on $X$, the pullback $f^*\mcl$ is ample.
Indeed, for a coherent sheaf $\mathcal F$ on $Y$, the sheaf $f_*\mathcal F$ is coherent by [[P-AGH255PUSHCOH]].
For large $n$, pull back the global generators of $f_*\mathcal F\otimes\mcl^{\otimes n}$ and use the surjection $f^*f_*\mathcal F\to\mathcal F$ to generate $\mathcal F\otimes(f^*\mcl)^{\otimes n}$.
On $f^{-1}(\Spec A)=\Spec B$, with $\mathcal F$ represented by a finite $B$-module $M$, this surjection is $B\otimes_A M\to M$, $b\otimes m\mapsto bm$.
:::

::: {.example title="An arbitrary twist need not remain ample"}
On $\PP_k^1$, the sheaf $\OO(1)$ is ample, but $\OO(1)\otimes\OO(-2)\cong\OO(-1)$ is not.
Every positive tensor power of $\OO(-1)$ has no global sections, so it fails the ample global-generation condition even with the coherent sheaf $\OO_{\PP^1}$ [@Har10a, Proposition II.5.13].
:::

::: {.example title="Degree on an elliptic curve"}
On a smooth projective genus-one curve over an algebraically closed field, an invertible sheaf of degree one is ample and has $h^0=1$, so its complete linear system does not give an embedding.
An invertible sheaf on this curve is very ample exactly when its degree is at least three; degree three embeds it as a plane cubic [@Har10a, Chapter IV, §§1 and 3].
:::

::: {.definition title="Hyperplane section"}
For a projective integral variety $X\subseteq\PP_k^n$ and a hyperplane $H$ not containing $X$, the \dfn{hyperplane section} $X\cap H$ is the effective Cartier divisor cut out by the restricted linear form.
Its associated invertible sheaf is $\OO_X(1)$.
Over an algebraically closed field, the hyperplane sections form the linear system $\PP V\subseteq\abs{\OO_X(1)}$, where $V$ is the image of $H^0(\PP_k^n,\OO(1))\to H^0(X,\OO_X(1))$ [@Har10a, Chapter II, §7].
:::
