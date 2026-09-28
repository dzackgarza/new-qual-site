---
schema: qual/card@1
id: P-AZOFF-B07
kind: problem
title: Implicit function theorem from the inverse function theorem
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Several variables, Problem 7, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Stated the finite-dimensional C^r implicit function theorem for
    F:R^n x R^m -> R^m with invertible partial derivative in the y variables.
    Derived it from the inverse function theorem by applying that theorem to
    H(x,y)=(x,F(x,y)); DH is block triangular with invertible diagonal blocks.
    The local inverse has form (x,G(x,z)), and phi(x)=G(x,F(a,b)) gives the
    implicit graph and derivative formula. The source compilation contains no
    worked solution.
---

::: {.problem}
State the most general (real) version of the implicit theorem you know and outline how it can be proved from the corresponding version of the (real) inverse function theorem.
:::

::: {.solution}
Let
$$
U\subseteq\RR^n\times\RR^m
$$
be open, let
$$
F:U\longrightarrow\RR^m
$$
be $C^r$ for some $1\leq r\leq\infty$, and let
$$
(a,b)\in U.
$$
Put
$$
c=F(a,b).
$$

<1>1. If the partial derivative
$$
D_yF(a,b):\RR^m\longrightarrow\RR^m
$$
is invertible, then there are neighborhoods
$$
a\in A\subseteq\RR^n,
\qquad
b\in B\subseteq\RR^m
$$
and a unique $C^r$ map
$$
\phi:A\longrightarrow B
$$
with $\phi(a)=b$ such that, for $(x,y)\in A\times B$,
$$
\boxed{
F(x,y)=c
\quad\Longleftrightarrow\quad
y=\phi(x).
}
$$
Moreover,
$$
D\phi(x)
=
-\bigl(D_yF(x,\phi(x))\bigr)^{-1}
D_xF(x,\phi(x))
$$
after the neighborhoods are chosen sufficiently small.

<2>1. Define
$$
H:U\longrightarrow\RR^n\times\RR^m,
\qquad
H(x,y)=(x,F(x,y)).
$$
Then
$$
DH(a,b)
=
\begin{pmatrix}
I_n&0\\
D_xF(a,b)&D_yF(a,b)
\end{pmatrix}
$$
is invertible.

::: {.proof}
The displayed derivative follows directly from the two components of $H$.
It is block lower triangular. Its diagonal blocks are $I_n$ and
$D_yF(a,b)$, both invertible, so $DH(a,b)$ is invertible.
:::

<2>2. The inverse function theorem gives neighborhoods
$$
(a,b)\in W\subseteq U,
\qquad
(a,c)\in Z\subseteq\RR^n\times\RR^m
$$
such that
$$
H|_W:W\longrightarrow Z
$$
is a $C^r$ diffeomorphism.

::: {.proof}
Step <2>1 is exactly the invertibility hypothesis of the inverse function
theorem at $(a,b)$.
:::

<2>3. After shrinking $Z$ to a product neighborhood if necessary, the local
inverse has the form
$$
H^{-1}(x,z)=(x,G(x,z))
$$
for a $C^r$ map $G$.

::: {.proof}
Because $Z$ is open and contains $(a,c)$, it contains a product
$$
A_0\times C
$$
of neighborhoods of $a$ and $c$. Restrict the inverse to this product.

If
$$
H(u,v)=(x,z),
$$
then the first component of the definition of $H$ gives $u=x$. Therefore
the first component of $H^{-1}(x,z)$ is always $x$, so the inverse has the
displayed form. Since $H^{-1}$ is $C^r$, so is $G$.
:::

<2>4. Define
$$
\phi(x)=G(x,c).
$$
After shrinking $A_0$ to a neighborhood $A$ of $a$ and choosing a
neighborhood $B$ of $b$, one has
$$
\phi:A\to B
$$
and, for $(x,y)\in A\times B$,
$$
F(x,y)=c
\quad\Longleftrightarrow\quad
y=\phi(x).
$$

::: {.proof}
Since
$$
H^{-1}(a,c)=(a,b),
$$
we have $G(a,c)=b$. Since $W$ is open, choose neighborhoods $A_1$ of $a$
and $B$ of $b$ such that
$$
A_1\times B\subseteq W.
$$
By continuity of $x\mapsto G(x,c)$ at $a$, shrink to a neighborhood
$$
A\subseteq A_0\cap A_1
$$
such that $\phi(A)\subseteq B$. Then $A\times B\subseteq W$ as required.

For $x\in A$,
$$
H(x,\phi(x))
=
H(H^{-1}(x,c))
=
(x,c),
$$
so
$$
F(x,\phi(x))=c.
$$

Conversely, if $(x,y)\in A\times B$ and $F(x,y)=c$, then
$$
H(x,y)=(x,c).
$$
Since $H|_W$ is injective and
$$
H(x,\phi(x))=(x,c),
$$
we get $y=\phi(x)$. This proves the local graph description and uniqueness.
:::

<2>5. The derivative of the implicit function is
$$
D\phi(x)
=
-\bigl(D_yF(x,\phi(x))\bigr)^{-1}
D_xF(x,\phi(x)).
$$

::: {.proof}
By continuity of $D_yF$ and invertibility at $(a,b)$, the neighborhoods may
be shrunk so that
$$
D_yF(x,\phi(x))
$$
is invertible for every $x\in A$. Differentiate the identity
$$
F(x,\phi(x))=c.
$$
The chain rule gives
$$
D_xF(x,\phi(x))
+
D_yF(x,\phi(x))D\phi(x)
=
0.
$$
Multiplying by the inverse of $D_yF(x,\phi(x))$ gives the formula.
:::

<2>6. Q.E.D.

::: {.proof}
Steps <2>1--<2>5 derive every assertion of step <1>1 from the inverse
function theorem.
:::

<1>2. Q.E.D.

::: {.proof}
Step <1>1 states the theorem for all finite $n,m$ and every order $1\leq r\leq\infty$, and its substeps derive it from the inverse function theorem.
:::
:::
