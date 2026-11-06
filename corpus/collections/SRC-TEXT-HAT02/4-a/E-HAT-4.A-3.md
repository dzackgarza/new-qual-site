---
schema: qual/card@1
id: E-HAT-4.A-3
kind: problem
title: "Automorphisms of $K(\\pi, 1)$ are outer automorphisms of $\\pi$"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.A, Exercise 3 and Proposition 4A.2; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
For a space $X$ let $\operatorname{Aut}(X)$ denote the group of homotopy classes of homotopy equivalences $X \to X$.
Show that for a CW complex $K(\pi, 1)$, $\operatorname{Aut}(K(\pi, 1))$ is isomorphic to the group of outer automorphisms of $\pi$, that is, automorphisms modulo inner automorphisms.
:::

::: {.solution}
Let $K=K(\pi,1)$. A self-homotopy equivalence $f:K\to K$ induces an automorphism
$$
f_*:\pi_1(K,x_0)\longrightarrow \pi_1(K,f(x_0)).
$$
After choosing a path from $f(x_0)$ back to $x_0$, this becomes an automorphism of $\pi$ via the change-of-basepoint isomorphism $\beta_\gamma$ (§4.1, p. 341), which is a homomorphism and satisfies $\beta_{\gamma\eta}=\beta_\gamma\beta_\eta$ (p. 342). Changing the path changes the resulting automorphism by an inner automorphism. Hence there is a well-defined homomorphism
$$
\Phi:\operatorname{Aut}(K)\longrightarrow\operatorname{Out}(\pi).
$$

Conversely, the free homotopy classes of maps $K\to K$ are computed by Proposition 1B.9 (p. 90), which classifies based maps into a $K(\pi,1)$ by their induced homomorphisms, together with Proposition 4A.2 (p. 422), which identifies $[Z,X]$ with the orbit set $\langle Z,X\rangle/\pi_1(X)$; for $X=K(\pi,1)$ this orbit set is the set of homomorphisms modulo inner automorphisms, so
$$
[K,K]\cong \operatorname{Hom}(\pi,\pi)/\operatorname{Inn}(\pi).
$$
Also the homotopy type of $K(\pi,1)$ is determined by $\pi$ (Theorem 1B.8, p. 90), so $\operatorname{Aut}(K(\pi,1))$ depends only on $\pi$.
Under this bijection, a map is a homotopy equivalence exactly when its induced endomorphism of $\pi$ is an automorphism. Indeed, if $f_*$ is an automorphism, choose a map $g:K\to K$ inducing $f_*^{-1}$; then $gf$ and $fg$ induce the identity outer automorphism, hence are freely homotopic to the identity. Thus $f$ is a homotopy equivalence.

Therefore the preceding bijection restricts to a bijection
$$
\operatorname{Aut}(K)\xrightarrow{\cong}\operatorname{Aut}(\pi)/\operatorname{Inn}(\pi),
$$
and composition corresponds to composition of outer automorphisms. Hence
$$
\boxed{\operatorname{Aut}(K(\pi,1))\cong\operatorname{Out}(\pi).}
$$
:::
