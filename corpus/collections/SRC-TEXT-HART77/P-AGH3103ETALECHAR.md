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
- event: source-checked
  by: claude
  date: 2026-11-09
  note: 'Read III.10.3 against Hartshorne p. 275 and Dongryul Kim, Solutions to Hartshorne, pp. 195-196. Repaired the converse of the differential criterion: the card asserted a zero-dimensional unramified criterion without proof. Step s1b now proves it, by the vanishing of Omega_{kappa(x)/kappa(y)} (II.8.6A for separability), by dim O_{X_y,x} = trdeg = 0, and by the square-zero thickening argument of Kim, which forces the local ring of the fibre to be a field. Also removed a pf-step block whose opening line carried no label and whose content duplicated the closing step.'
---

::: {.problem}
A morphism $f: X \to Y$ of schemes of finite type over $k$ is \dfn{étale} if it is smooth of relative dimension $0$.
It is \dfn{unramified} if for every $x \in X$, letting $y = f(x)$, we have $\mfm_y \cdot \mco_x = \mfm_x$, and $k(x)$ is a separable algebraic extension of $k(y)$.

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

For a morphism locally of finite type, unramifiedness at $x$ implies
$$
(\Omega_{X/Y})_x=0.
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

Suppose that $f$ is unramified at $x$. Then
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

:::

:::

::: {.pf-step #s1b}

Conversely, $(\Omega_{X/Y})_x=0$ implies that $f$ is unramified at $x$; hence,
for a morphism locally of finite type, unramifiedness is equivalent to the
vanishing of $\Omega_{X/Y}$.

::: pf-proof

Keep the notation of step [](#s1){.pf-ref}, and assume $(\Omega_{X/Y})_x=0$. Then
$\Omega_{R/\kappa}=0$. Applying II.8.4A to the maximal ideal $\mfm_R$ of $R$
gives a surjection $\Omega_{R/\kappa}\tensor_R\kappa(x)\to\Omega_{\kappa(x)/\kappa}\to0$,
so $\Omega_{\kappa(x)/\kappa}=0$. The point $x$ lies on the fibre $X_y$, which is
of finite type over $\kappa(y)$, so $\kappa(x)$ is a finitely generated field
extension of $\kappa$; by Theorem II.8.6A, $\Omega_{\kappa(x)/\kappa}=0$ forces
$\kappa(x)/\kappa$ to be algebraic, hence finite and separable.
Since $\dim\OO_{X_y,x}=\operatorname{tr\,deg}_{\kappa}\kappa(x)=0$ for a scheme
of finite type over a field, the fibre $X_y$ is zero-dimensional at $x$.

It remains to see that $R$ is a field. Base change to an algebraic closure of
$\kappa$ does not change $\Omega$ (Proposition II.8.10), so we may assume that
$\kappa$ is algebraically closed. Then $R$ is a zero-dimensional local ring
essentially of finite type over $\kappa$. Put $\mfm=\mfm_R$ and apply II.8.4A to
the ideal $\mfm^2$: the exact sequence
$$
\mfm^2/\mfm^4
\longrightarrow
\Omega_{R/\kappa}\tensor_R(R/\mfm^2)
\longrightarrow
\Omega_{(R/\mfm^2)/\kappa}
\longrightarrow 0
$$
has vanishing middle term, so $\Omega_{(R/\mfm^2)/\kappa}=0$. But
$R/\mfm^2\cong\kappa[\epsilon_1,\ldots,\epsilon_m]/(\epsilon_1,\ldots,\epsilon_m)^2$
with $m=\dim_\kappa\mfm/\mfm^2$, and for that ring
$$
\Omega\tensor\kappa\cong\kappa^{\oplus m},
\qquad
d\epsilon_i\longmapsto e_i,
$$
so $m=0$. Thus $\mfm=\mfm^2$, and Nakayama's lemma gives $\mfm=0$: $R$ is a
field, so $R$ equals its residue field $\kappa(x)$.
Undoing the field extension, $R$ is a field whose residue field is separable
over $\kappa$, and $R=\kappa(x)$ says exactly that $\mfm_x=\mfm_yB$, which is
Hartshorne's local definition of unramifiedness.
Since $x$ was arbitrary, $f$ is unramified.

This is the differential characterization recorded in [[D-MORUNR]].

:::

:::

::: {.pf-step #s2}

Conditions (ii) and (iii) are equivalent.

::: pf-proof

Both conditions require $f$ to be flat. By steps [](#s1){.pf-ref} and [](#s1b){.pf-ref},
their remaining conditions
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

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s1b){.pf-ref} identify vanishing relative differentials with Hartshorne's
unramified condition, so with the flatness hypothesis shared by (ii) and (iii)
they give (ii) $\Longleftrightarrow$ (iii). Step [](#s3){.pf-ref} gives
(i) $\Longrightarrow$ (ii), and steps [](#s4){.pf-ref} and [](#s5){.pf-ref} give
(iii) $\Longrightarrow$ (i). Hence the three conditions are equivalent:
$$
\boxed{\text{(i)}\iff\text{(ii)}\iff\text{(iii)}}.
$$

:::

:::

:::

::: {.remark title="Published solution"}
Dongryul Kim, *Solutions to Hartshorne's Algebraic Geometry* (Chapters II--III), Chapter III §10, Exercise 10.3, PDF pp. 195--196, source revision `6c627eed7b0226249df79b8777f5ac450f17885a`: for (ii) implies (iii) he shows $\Omega_{X_y/\kappa(y)}=0$, hence $\Omega_{\kappa(x)/\kappa(y)}=0$ and a finite separable residue extension, and then proves the fibre reduced by the square-zero thickening: $\mathfrak m^2/\mathfrak m^4\to\Omega\otimes(A/\mathfrak m^2)\to\Omega_{(A/\mathfrak m^2)/k}\to0$ with $\Omega_{(k[\epsilon]/\epsilon^2)/k}\otimes k\cong k^{\oplus m}$ forcing $m=0$; (iii) implies (i) is then Theorem 3.10.2. The proof above now contains exactly that reducedness argument as step s1b, in place of the assertion of a "zero-dimensional unramified criterion" that it made before; (i) implies (ii) and (iii) implies (i) agree with Kim's steps.
:::
