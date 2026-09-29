---
schema: qual/card@1
id: P-AGH3103ETALECHAR
kind: problem
title: Characterizations of an etale morphism
classification:
  areas:
  - algebraic-geometry
  topics:
  - Smooth Morphisms
  - Etale Morphisms
  - Unramified Morphisms
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Exercise III.10.3 together with the differential criterion for
    unramified morphisms and the flat-plus-geometrically-regular-fibres
    criterion for smoothness. The proof checks the maximal-ideal and separable
    residue-field clauses on the local rings of the fibres.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
A morphism $f: X \to Y$ of schemes of finite type over $k$ is **étale** if it is smooth of relative dimension $0$.
It is **unramified** if for every $x \in X$, letting $y = f(x)$, we have $\mfm_y \cdot \mco_x = \mfm_x$, and $k(x)$ is a separable algebraic extension of $k(y)$.

Show that the following conditions are equivalent:

(i) $f$ is étale;

(ii) $f$ is flat, and $\Omega_{X/Y} = 0$;

(iii) $f$ is flat and unramified.
:::

::: {.solution}
Because $X$ and $Y$ are of finite type over $k$, the morphism $f$ is locally
of finite presentation.

::: pf

::: {.pf-step #s1}

For a morphism locally of finite type,
$$
f\text{ is unramified}
\quad\Longleftrightarrow\quad
\Omega_{X/Y}=0.
$$

::: pf-proof

Fix $x\in X$, put $y=f(x)$, and write
$$
A=\OO_{Y,y},
\qquad
B=\OO_{X,x},
\qquad
\kappa=\kappa(y),
\qquad
K=\kappa(x).
$$
The local ring of the fibre $X_y$ at $x$ is
$$
R=(B/\mfm_yB)_{\mathfrak m_x/\mathfrak m_yB},
$$
and formation of relative differentials commutes with base change:
$$
\Omega_{R/\kappa}
\cong
(\Omega_{X/Y})_x\tensor_B R.
$$

Suppose first that $f$ is unramified at $x$. Then
$$
\mfm_yB=\mfm_x,
$$
so $R=K$. The extension $K/\kappa$ is finite separable by definition.
Therefore
$$
\Omega_{R/\kappa}=\Omega_{K/\kappa}=0.
$$
Nakayama's lemma applied to the finite $B$-module
$(\Omega_{X/Y})_x$ now gives
$$
(\Omega_{X/Y})_x=0.
$$

Conversely, suppose $(\Omega_{X/Y})_x=0$. Then
$$
\Omega_{R/\kappa}=0.
$$
For a local algebra essentially of finite type over a field, vanishing of
the module of differentials is the zero-dimensional unramified criterion:
the local ring is its residue field and that residue field is finite separable
over the base field. Thus
$$
R=K,
\qquad
K/\kappa\text{ finite separable}.
$$
The equality $R=K$ means that the maximal ideal of $R$ is zero, i.e.
$$
\mfm_x/\mfm_yB=0.
$$
Hence
$$
\mfm_yB=\mfm_x,
$$
which is exactly Hartshorne's local definition of unramifiedness at $x$.

Since this holds at every point,
$$
\boxed{f\text{ unramified}\iff\Omega_{X/Y}=0}.
$$
This is the differential characterization recorded in [[D-MORUNR]].

:::

:::

::: {.pf-step #s2}

Conditions (ii) and (iii) are equivalent.

::: pf-proof

Both conditions require $f$ to be flat. By step [](#s1){.pf-ref}, their remaining
conditions
$$
\Omega_{X/Y}=0
\qquad\text{and}\qquad
f\text{ unramified}
$$
are equivalent. Hence
$$
\boxed{\text{(ii)}\iff\text{(iii)}}.
$$

:::

:::

::: {.pf-step #s3}

Condition (i) implies condition (ii).

::: pf-proof

If $f$ is étale in the sense of the problem, it is smooth of relative
dimension zero. A smooth morphism is flat, and for a smooth morphism of
relative dimension $r$ the sheaf of relative differentials is locally free of
rank $r$ [[D-MORSM|by the differential criterion for smoothness]].
Here $r=0$, so
$$
\Omega_{X/Y}=0.
$$
Thus (ii) holds.

:::

:::

::: {.pf-step #s4}

If condition (iii) holds, then every fibre of $f$ is geometrically regular of dimension zero.

::: pf-proof

Assume $f$ is flat and unramified. Fix $x\in X$ and put $y=f(x)$.
As in step [](#s1){.pf-ref}, the local ring of the fibre at $x$ is
$$
\OO_{X_y,x}
=(\OO_{X,x}/\mfm_y\OO_{X,x})_{\mathfrak m_x/\mathfrak m_y\OO_{X,x}}.
$$
Unramifiedness gives
$$
\mfm_y\OO_{X,x}=\mfm_x,
$$
so
$$
\OO_{X_y,x}=\kappa(x).
$$
Moreover $\kappa(x)/\kappa(y)$ is finite separable.

After any field extension $L/\kappa(y)$, the algebra
$$
\kappa(x)\tensor_{\kappa(y)}L
$$
is finite étale over $L$ after passage to the corresponding field factors;
in particular all its local rings are fields. Thus the fibre remains regular
after every field extension. Hence $X_y$ is geometrically regular of pure
dimension zero at $x$.
Since $x$ was arbitrary, every fibre is geometrically regular of dimension
zero.

:::

:::

::: {.pf-step #s5}

Condition (iii) implies condition (i).

::: pf-proof

Under (iii), $f$ is flat by hypothesis and locally of finite presentation
because it is a morphism between schemes of finite type over $k$.
Step [](#s4){.pf-ref} shows that all fibres are geometrically regular of pure dimension
zero. The fibre criterion for smoothness [[D-MORSM]] therefore says that $f$
is smooth of relative dimension zero.
By definition, $f$ is étale. Thus
$$
\boxed{\text{(iii)}\Longrightarrow\text{(i)}}.
$$

:::

:::

::: pf-step

The three conditions are equivalent.

::: pf-proof

Step [](#s3){.pf-ref} gives
$$
\text{(i)}\Longrightarrow\text{(ii)},
$$
step [](#s2){.pf-ref} gives
$$
\text{(ii)}\Longleftrightarrow\text{(iii)},
$$
and step [](#s5){.pf-ref} gives
$$
\text{(iii)}\Longrightarrow\text{(i)}.
$$
Therefore
$$
\boxed{\text{(i)}\iff\text{(ii)}\iff\text{(iii)}}.
$$

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} identify vanishing relative differentials with Hartshorne's
unramified condition, and steps [](#s3){.pf-ref}, [](#s4){.pf-ref} and [](#s5){.pf-ref} identify flat unramified morphisms
with smooth morphisms of relative dimension zero.

:::

:::

:::
