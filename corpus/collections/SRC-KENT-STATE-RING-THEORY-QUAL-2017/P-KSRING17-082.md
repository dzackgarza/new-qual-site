---
schema: qual/card@1
id: P-KSRING17-082
kind: problem
title: '$\ZZ[\sqrt 5]$ is not a UFD: irreducibility of $x^2+x-1$'
classification:
  areas: [algebra]
  topics:
  - Quadratic Integer Rings
  - Unique Factorization Domains
  - Gauss's Lemma
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 82 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Replaced the OCR-garbled dash and closing clause of the definition of D against problem 82 on Ring_Theory_Qual_Problems.pdf PDF page 12.
---

::: {.problem}
Let $D = \ZZ[\sqrt{5}] = \{ m + n\sqrt{5} \mid m, n \in \ZZ \}$ — a subring of the field of real numbers and necessarily an integral domain (you need not show this) — and $F = \QQ(\sqrt{5})$ its field of fractions.
Show the following:

(a) $x^2 + x - 1$ is irreducible in $D[x]$ but not in $F[x]$.

(b) $D$ is not a unique factorization domain.
:::

::: {.solution}

Set
$$
f(x)
\coloneqq
x^2+x-1.
$$

::: pf

::: {.pf-step #s1-1}

In the field
$$
F=\QQ(\sqrt5),
$$
the polynomial $f$ factors as
$$
\boxed{
f(x)
=
\left(
x-\frac{-1+\sqrt5}{2}
\right)
\left(
x-\frac{-1-\sqrt5}{2}
\right).
}
$$


::: pf-proof

The quadratic formula gives the two roots
$$
\alpha
\coloneqq
\frac{-1+\sqrt5}{2},
\qquad
\beta
\coloneqq
\frac{-1-\sqrt5}{2}.
$$
Both lie in
$$
\QQ(\sqrt5)=F.
$$
Therefore
$$
f(x)
=(x-\alpha)(x-\beta)
$$
in
$$
F[x].
$$
Thus $f$ is reducible over $F$.

:::

:::

::: {.pf-step #s1-2}

Neither root $\alpha$ nor $\beta$ belongs to
$$
D=\ZZ[\sqrt5].
$$


::: pf-proof

Suppose
$$
\alpha
=
m+n\sqrt5
$$
for integers
$$
m,n.
$$
Then
$$
-\frac12
+
\frac12\sqrt5
=
m+n\sqrt5.
$$
Because
$$
1
\qquad\text{and}\qquad
\sqrt5
$$
are linearly independent over $\QQ$, comparison of coefficients gives
$$
m=-\frac12,
\qquad
n=\frac12,
$$
contradicting
$$
m,n\in\ZZ.
$$
Thus
$$
\alpha\notin D.
$$

The same argument applied to
$$
\beta
=
-\frac12
-
\frac12\sqrt5
$$
shows
$$
\beta\notin D.
$$

:::

:::

::: {.pf-step #s1-3}

If a monic quadratic polynomial over an integral domain $A$ is reducible in $A[x]$, then it has a root in $A$.


::: pf-proof

Let
$$
g(x)
=
x^2+cx+d
\in
A[x]
$$
be monic and reducible.
Because $A$ is a domain, degrees add under multiplication, so a nontrivial factorization has the form
$$
g(x)
=
(ux+a)(vx+b)
$$
with
$$
u,v,a,b\in A
$$
and
$$
uv=1
$$
because $g$ is monic.
Thus $u$ and $v$ are units.
Set
$$
a'
\coloneqq
u^{-1}a,
\qquad
b'
\coloneqq
v^{-1}b.
$$
Then
$$
\begin{aligned}
g(x)
&=
uv(x+a')(x+b')\\
&=
(x+a')(x+b').
\end{aligned}
$$
Hence
$$
-a'
$$
is a root of $g$ in $A$.

:::

:::

::: {.pf-step #s1-4}

The polynomial
$$
x^2+x-1
$$
is irreducible in
$$
D[x].
$$


::: pf-proof

The ring $D$ is an integral domain by hypothesis.
If
$$
f(x)
$$
were reducible in
$$
D[x],
$$
step [](#s1-3){.pf-ref} would imply that it has a root in $D$.
Its only roots in the fraction field are
$$
\alpha
\qquad\text{and}\qquad
\beta,
$$
and step [](#s1-2){.pf-ref} shows that neither lies in $D$.
Therefore $f$ is irreducible in $D[x]$.

:::

:::

::: {.pf-step #s1-5}

Thus
$$
\boxed{
x^2+x-1
\text{ is irreducible in }D[x]
\text{ but reducible in }F[x].
}
$$


::: pf-proof

Irreducibility over $D$ is step [](#s1-4){.pf-ref}, while reducibility over $F$ is step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

The element
$$
\alpha
=
\frac{-1+\sqrt5}{2}
$$
is integral over $D$ but does not lie in $D$.


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
f(\alpha)=0,
$$
where
$$
f(x)=x^2+x-1
$$
is monic with coefficients in
$$
\ZZ\subseteq D.
$$
Hence $\alpha$ is integral over $D$.
Step [](#s1-2){.pf-ref} shows
$$
\alpha\notin D.
$$

:::

:::

::: {.pf-step #s1-7}

Every UFD is integrally closed in its field of fractions.


::: pf-proof

Let
$$
A
$$
be a UFD and let
$$
\frac ab
\in
\operatorname{Frac}(A)
$$
be integral over $A$, written so that $a$ and $b$ have no common irreducible factor.
Choose a monic equation
$$
\left(\frac ab\right)^n
+
c_{n-1}\left(\frac ab\right)^{n-1}
+
\cdots
+
c_0
=
0
$$
with
$$
c_i\in A.
$$
Multiplying by
$$
b^n
$$
gives
$$
a^n
=
-b
\left(
c_{n-1}a^{n-1}
+
c_{n-2}a^{n-2}b
+
\cdots
+
c_0b^{n-1}
\right).
$$
Thus
$$
b\mid a^n.
$$
If $b$ were not a unit, some irreducible
$$
\pi
$$
would divide $b$.
In a UFD irreducibles are prime, so
$$
\pi\mid a^n
$$
would imply
$$
\pi\mid a,
$$
contradicting the choice of $a,b$ with no common irreducible factor.
Therefore
$$
b
$$
is a unit, so
$$
a/b\in A.
$$
Hence $A$ is integrally closed.

:::

:::

::: {.pf-step #s1-8}

The ring $D$ is not a UFD.


::: pf-proof

By step [](#s1-6){.pf-ref}, there is an element of
$$
\operatorname{Frac}(D)=F
$$
that is integral over $D$ but does not lie in $D$.
Thus $D$ is not integrally closed.
By step [](#s1-7){.pf-ref}, every UFD is integrally closed.
Therefore
$$
\boxed{
D\text{ is not a unique factorization domain}.
}
$$

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} proves part (a), and step [](#s1-8){.pf-ref} proves part (b).

:::

:::

:::
