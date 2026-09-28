---
schema: qual/card@1
id: P-BERK81S-13
kind: problem
title: Surjectivity of $I-vu$ follows from surjectivity of $I-uv$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    For a target y, surjectivity of h gives x with
    x-u(v(x))=u(y). Applying v yields
    v(x)-v(u(v(x)))=v(u(y)). Then z=y+v(x) satisfies
    f(z)=y by direct expansion.
---

::: {.problem}
Let $G$ be an additive group and let $u,v:G\to G$ be homomorphisms.
Define
\[
f(x)=x-v(u(x)),
\qquad
h(x)=x-u(v(x)).
\]
Show that if $h$ is surjective, then $f$ is surjective.
:::

::: {.solution}
<1>1. Fix an arbitrary element
$$
y\in G.
$$

::: {.proof}
To prove surjectivity of $f$, it suffices to construct an element
$z\in G$ such that
$$
f(z)=y.
$$
:::

<1>2. Since $h$ is surjective, there is an element $x\in G$ such that
$$
x-u(v(x))=u(y).
$$

::: {.proof}
Apply surjectivity of
$$
h(x)=x-u(v(x))
$$
to the element $u(y)\in G$.
:::

<1>3. Applying $v$ to the equality in step <1>2 gives
$$
v(x)-v(u(v(x)))=v(u(y)).
$$

::: {.proof}
The map $v:G\to G$ is a group homomorphism, so it preserves subtraction:
$$
\begin{aligned}
v\bigl(x-u(v(x))\bigr)
&=
v(x)-v(u(v(x))).
\end{aligned}
$$
Apply $v$ to both sides of the equality in step <1>2.
:::

<1>4. Define
$$
z=y+v(x).
$$
Then
$$
\boxed{
f(z)=y.
}
$$

::: {.proof}
Using additivity of $u$ and $v$,
$$
\begin{aligned}
f(z)
&=
z-v(u(z))\\
&=
y+v(x)-v\bigl(u(y+v(x))\bigr)\\
&=
y+v(x)-v(u(y))-v(u(v(x)))\\
&=
y
+
\bigl(
v(x)-v(u(v(x)))-v(u(y))
\bigr).
\end{aligned}
$$
The parenthesized term is zero by step <1>3. Hence $f(z)=y$.
:::

<1>5. The map $f$ is surjective.

::: {.proof}
The element $y\in G$ in step <1>1 was arbitrary, and step <1>4 constructs
a preimage $z$ of it under $f$. Therefore every element of $G$ lies in the
image of $f$.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
