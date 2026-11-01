---
schema: qual/card@1
id: E-SSA.PR-5
kind: problem
title: "The exact formula for $p(n)$: the transformation at every rational point"
classification:
  areas:
  - complex-analysis
  topics:
  - Partitions
  - Modular Forms
  - Asymptotics
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    Statement transcribed from Stein--Shakarchi, *Complex Analysis*, Appendix A, §5, problem 5,
    read from `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf` (PDF pages 359--363, printed
    pages 341--343). This card did not exist before: the collection had no appendix directory at all,
    and a completeness audit against the book found Appendix A's whole Problems section, items 1--5,
    missing. The transcription was taken from the OCR text layer and cleaned of OCR errors; the
    printed wording, hypotheses and bracketed hints are preserved.
- event: solution-written
  by: claude
  date: 2026-11-01
  note: >-
    Solution installed up to, but not including, the exercise's final sentence. Proved: the multiplier system of eta on SL2(Z) with values in mu_24 by Euclidean descent, the transformation at every rational p/q with a constant of modulus one and order dividing 24q, and the resulting contribution of p/q to the asymptotic formula. **Left open on the card:** the convergence of the resulting series and hence the exact formula for p(n), which needs the Farey dissection, uniform arc estimates and Rademacher's theorem; the book's own error term is larger than every q >= 2 contribution, so its estimates cannot supply this. This is recorded as open, not claimed.
---

::: {.exercise}
The one shortcoming in our derivation of the asymptotic formula for $p(n)$ arose from the fact that while $f_1(z)=\frac{z}{i}e^{\frac{\pi i}{12z}}e^{\frac{\pi iz}{12}}$ is a good approximation to the generating function $f(z)$ near $z=0$, this fails near other points on the real axis, since $f_1$ is regular there, but $f$ is not.

However, using the transformation law (24) and the identity $f(z+1)=f(z)$, one can derive the following generalization of (24): whenever $p/q$ is a rational number in lowest form (so $p$ and $q$ are relatively prime) then
$$
f\Bigl(z-\frac{p}{q}\Bigr)=\omega_{p/q}\Bigl(\frac{zq}{i}\Bigr)^{1/2}e^{\frac{\pi i}{12zq^2}}e^{-\frac{\pi iz}{12}}f\Bigl(-\frac{1}{zq^2}-\frac{p'}{q}\Bigr),
$$
where $pp'\equiv1 \pmod q$. Here $\omega_{p/q}$ is an appropriate $24$th root of unity. This formula leads to an analogous $f_{p/q}$, approximating $f$ at $z=p/q$.

From this one can obtain for each $p/q$ a contribution of the form
$$
c_{p/q}\frac{1}{2\pi\sqrt{2}}\frac{d}{dn}\Bigl[\frac{e^{\frac{K}{q}(n-\frac{1}{24})^{1/2}}}{(n-\frac{1}{24})^{1/2}}\Bigr]
$$
to the asymptotic formula for $p(n)$. When suitably modified, the resulting series, summed over all proper fractions $p/q$ in $[0,1)$, actually converges and gives an exact formula for $p(n)$.
:::

::: {.solution}

**What the exercise states, and what is proved below.** The exercise asks for three things: (i) the
transformation law for $f$ at an arbitrary rational point $p/q$, generalizing (24); (ii) the
contribution that the point $p/q$ then makes to the asymptotic formula for $p(n)$; (iii) the remark
that the resulting series, "suitably modified", converges and gives an exact formula for $p(n)$.

Below, (i) is proved (Theorem 2), with the corrections to the printed statement that the derivation
forces; (ii) is proved (Theorem 3), including the exact constant $1/(2\pi\sqrt2)$ and the
$q$-dependence; (iii) is *not* proved, neither here nor in the book — the last section lists
precisely what is missing. So the block is complete for (i) and (ii) and explicitly incomplete
for (iii).

Throughout $z=x+iy\in\HH$ (the upper half plane),
$$
\eta(z)=e^{\pi iz/12}\prod_{n\ge1}\bigl(1-e^{2\pi inz}\bigr),\qquad
f(z)=\frac{e^{\pi iz/12}}{\eta(z)}=\sum_{n\ge0}p(n)e^{2\pi inz},
$$
the last identity being the Euler product of Theorem 2.1, Chapter 10. We use three facts from the
book:

* **(24)**, i.e. $f(z)=(z/i)^{1/2}e^{\pi i/(12z)}e^{\pi iz/12}f(-1/z)$, which is
  $\eta(-1/z)=(z/i)^{1/2}\eta(z)$, Proposition 1.9 of Chapter 10;
* **(25)**, i.e. $f(z)=1+O(e^{-2\pi y})$ for $y\ge1$;
* $f(z+1)=f(z)$, which is immediate from the series.

Set $K=\pi\sqrt{2/3}$ and $\lambda=\lambda_n=(n-\tfrac1{24})^{1/2}$ for $n\ge1$; thus
$K=\pi\sqrt{2/3}=2\pi/\sqrt6$ and $\lambda^2=n-\tfrac1{24}$.

## 1. The transformation law at every rational point

The printed statement is
$$
f\Bigl(z-\frac pq\Bigr)=\omega_{p/q}\Bigl(\frac{zq}{i}\Bigr)^{1/2}
e^{\frac{\pi i}{12zq^2}}e^{-\frac{\pi iz}{12}}f\Bigl(-\frac{1}{zq^2}-\frac{p'}{q}\Bigr),
\qquad pp'\equiv 1\ (\mathrm{mod}\ q),
$$
with $\omega_{p/q}$ "an appropriate $24$th root of unity". Theorem 2 proves this with the changes
recorded in Remark 3: the exponent $e^{-\pi iz/12}$ must be $e^{+\pi iz/12}$, the variable must be
the shifted one, and $\omega_{p/q}$ is a root of unity of order dividing $24q$.

**Lemma 1 (multiplier of $\eta$).** Let $\gamma=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in SL_2(\ZZ)$
with $c>0$. Then there is a constant $\varepsilon(\gamma)\in\mu_{24}:=\{\zeta:\zeta^{24}=1\}$ such
that
$$
\eta(\gamma z)=\varepsilon(\gamma)\,(cz+d)^{1/2}\,\eta(z),\qquad z\in\HH,
$$
where $(cz+d)^{1/2}$ denotes the principal branch; it is holomorphic in $z$ because
$\operatorname{Im}(cz+d)=c\,\operatorname{Im}z>0$.

*Proof.* Write $T=\begin{pmatrix}1&1\\0&1\end{pmatrix}$ and $S=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$.
From the product, $\eta(z+1)=e^{\pi i/12}\eta(z)$, i.e. $\eta(z+m)=e^{\pi im/12}\eta(z)$ for
$m\in\ZZ$; and $\eta(-1/z)=(z/i)^{1/2}\eta(z)$ is Proposition 1.9 of Chapter 10.

We prove the lemma by strong induction on $c\ge0$. For $c=0$ we have $ad=1$, so $\gamma$ acts as
$z\mapsto z+m$ for some $m\in\ZZ$ and $\eta(\gamma z)=e^{\pi im/12}\eta(z)$, which is the assertion
with $\varepsilon=\pm e^{\pi im/12}\in\mu_{24}$ (the sign coming from
$(0\cdot z+d)^{1/2}=d^{1/2}=\pm1$).

Let $c>0$, choose $k\in\ZZ$ with $|a+kc|\le c/2$, and put
$$
\gamma_k:=ST^k\gamma=\begin{pmatrix}0&-1\\1&k\end{pmatrix}\begin{pmatrix}a&b\\c&d\end{pmatrix}
=\begin{pmatrix}-c&-d\\a+kc&b+kd\end{pmatrix}
=:\begin{pmatrix}a_k&b_k\\c_k&d_k\end{pmatrix},
\qquad |c_k|\le c/2<c .
$$
Further put $\gamma_1:=\begin{pmatrix}-k&-1\\1&0\end{pmatrix}\in SL_2(\ZZ)$, whose lower row is
$(1,0)$; then
$$
\gamma_1\gamma_k=\begin{pmatrix}-k&-1\\1&0\end{pmatrix}\begin{pmatrix}-c&-d\\a+kc&b+kd\end{pmatrix}
=\begin{pmatrix}-a&-b\\-c&-d\end{pmatrix}=-\gamma ,
$$
so $\gamma_1\gamma_k$ and $\gamma$ induce the same Möbius transformation.

First, $\eta(\gamma_1w)=\eta(-k-1/w)=e^{-\pi ik/12}\eta(-1/w)$, and
$e^{-\pi ik/12}(w/i)^{1/2}\eta(w)=\varepsilon(\gamma_1)w^{1/2}\eta(w)$ with
$\varepsilon(\gamma_1)=e^{-\pi ik/12}e^{-\pi i/4}\in\mu_{24}$, while $(c_1w+d_1)^{1/2}=w^{1/2}$.

Second, the induction hypothesis supplies $\varepsilon_k\in\mu_{24}$ with
$\eta(\gamma_kz)=\varepsilon_k(c_kz+d_k)^{1/2}\eta(z)$: if $c_k>0$ this is the hypothesis itself; if
$c_k<0$ apply the hypothesis to $-\gamma_k$, which induces the same map, and use
$(-c_kz-d_k)^{1/2}=\pm i\,(c_kz+d_k)^{1/2}$; if $c_k=0$ the base case applies with
$(c_kz+d_k)^{1/2}=d_k^{1/2}=\pm1$. In all three cases $\varepsilon_k\in\mu_{24}$ (note
$i=e^{\pi i/2}=(e^{\pi i/12})^6\in\mu_{24}$).

Now $\gamma z=\gamma_1(\gamma_kz)$, so
$$
\eta(\gamma z)=\varepsilon(\gamma_1)(\gamma_kz)^{1/2}\eta(\gamma_kz)
=\varepsilon(\gamma_1)\varepsilon_k\,(\gamma_kz)^{1/2}(c_kz+d_k)^{1/2}\eta(z).
$$
For a product $\gamma_1\gamma_k$ the matrix entries satisfy the cocycle identity
$c_{\gamma_1\gamma_k}z+d_{\gamma_1\gamma_k}=(c_1\gamma_kz+d_1)(c_kz+d_k)$; here the left-hand side
is $-(cz+d)$, so $(\gamma_kz)(c_kz+d_k)=-(cz+d)$ and therefore
$(\gamma_kz)^{1/2}(c_kz+d_k)^{1/2}=\pm(cz+d)^{1/2}$, the two sides having equal squares. Hence
$\eta(\gamma z)=\varepsilon(\gamma)(cz+d)^{1/2}\eta(z)$ with
$\varepsilon(\gamma)=\pm\varepsilon(\gamma_1)\varepsilon_k\in\mu_{24}$: a product of $24$th roots
of unity and signs is again a $24$th root of unity. The induction terminates because
$|c_k|\le c/2$. $\square$

**Theorem 2 (the generalization of (24)).** Let $p,q$ be coprime with $q\ge1$, let $p'\in\ZZ$ with
$pp'\equiv1\ (\mathrm{mod}\ q)$, and put $b=(pp'-1)/q\in\ZZ$ and
$\gamma=\begin{pmatrix}p&b\\q&p'\end{pmatrix}\in SL_2(\ZZ)$, so that $pp'-qb=1$. Then for every
$\xi\in\HH$,
$$
f\Bigl(\xi+\frac pq\Bigr)=\omega_{p/q}\Bigl(\frac{\xi q}{i}\Bigr)^{1/2}
\exp\Bigl(\frac{\pi i}{12q^2\xi}\Bigr)\exp\Bigl(\frac{\pi i\xi}{12}\Bigr)
f\Bigl(-\frac{1}{q^2\xi}-\frac{p'}{q}\Bigr),
$$
where, for the sign determined by the branches of the two square roots,
$$
\omega_{p/q}=\varepsilon(\gamma)^{-1}\bigl(\pm e^{-\pi i/4}\bigr)e^{\pi i(p+p')/(12q)} .
$$
In particular $|\omega_{p/q}|=1$ and $\omega_{p/q}^{24q}=1$; and $\omega_{p/q}$ does not depend on
which inverse $p'$ of $p$ modulo $q$ is chosen.

*Proof.* By Lemma 1, for $z\in\HH$,
$$
f(\gamma z)=\frac{e^{\pi i\gamma z/12}}{\eta(\gamma z)}
=\varepsilon(\gamma)^{-1}(qz+p')^{-1/2}e^{\pi i(\gamma z-z)/12}f(z).
$$
Put $w:=\gamma z$, so $z=\gamma^{-1}w=\dfrac{p'w-b}{-qw+p}$, and write $w=\xi+p/q$ with $\xi\in\HH$.
Then $qw-p=q\xi$ and, since $p'p-qb=1$,
$$
p'w-b=\frac{p'p}{q}-b+p'\xi=\frac1q+p'\xi,
\qquad\text{whence}\qquad
z=-\frac{1}{q^2\xi}-\frac{p'}{q}\in\HH
$$
(because $\operatorname{Im}\bigl(-1/(q^2\xi)\bigr)=y/(q^2|\xi|^2)>0$), and $qz+p'=-1/(q\xi)$;
moreover $f(z)$ is exactly the last factor in the assertion. Also
$$
\gamma z-z=w-z=\xi+\frac pq+\frac{1}{q^2\xi}+\frac{p'}{q},
$$
so $e^{\pi i(\gamma z-z)/12}=e^{\pi i/(12q^2\xi)}e^{\pi i\xi/12}e^{\pi i(p+p')/(12q)}$. Finally
$\bigl(-1/(q\xi)\bigr)^{-1/2}$ and $(\xi q/i)^{1/2}$ have the same modulus $(q|\xi|)^{1/2}$, and
their quotient is constant, because the two arguments differ by the constant factor
$-1/(q\xi)=i/(\xi q/i)$; thus the quotient is $\pm e^{-\pi i/4}$. Collecting,
$$
f\Bigl(\xi+\frac pq\Bigr)=\varepsilon(\gamma)^{-1}\bigl(\pm e^{-\pi i/4}\bigr)
e^{\pi i(p+p')/(12q)}\Bigl(\frac{\xi q}{i}\Bigr)^{1/2}
e^{\pi i/(12q^2\xi)}e^{\pi i\xi/12}f\Bigl(-\frac{1}{q^2\xi}-\frac{p'}{q}\Bigr).
$$
The factors $\varepsilon(\gamma)^{-1}$, $\pm e^{-\pi i/4}$ and $\pm1$ lie in $\mu_{24}$, while
$e^{\pi i(p+p')/(12q)}=\bigl(e^{2\pi i/(24q)}\bigr)^{p+p'}\in\mu_{24q}$; since $24\mid24q$ the
product lies in $\mu_{24q}$, and all factors have modulus $1$. Replacing $p'$ by $p'+q$ replaces $b$
by $b+p$ and hence changes $\gamma$ and $\varepsilon(\gamma)$, but it changes the argument of the
last $f$ only by the integer $-1$, and $f$ is $1$-periodic by the series; so $\omega_{p/q}$ does not
change. $\square$

For $p/q=0/1$ one may take $p'=0$, $b=-1$, $\gamma=S$; then the two constants cancel and Theorem 2
reads $f(\xi)=(\xi/i)^{1/2}e^{\pi i/(12\xi)}e^{\pi i\xi/12}f(-1/\xi)$ with $\omega_{0/1}=1$, i.e. it
*is* (24). That is the check the book makes.

**Remark 3 (what the derivation corrects in the printed statement).**

*(a) The sign.* As printed, the statement has $e^{-\pi iz/12}$ where Theorem 2 has
$e^{+\pi i\xi/12}$, and with the minus sign no constant $\omega_{p/q}$ can work. Indeed, take
$q=1$, $p=1$, $p'=1$: then $f(z-p/q)=f(z-1)=f(z)$ and $f(-1/(zq^2)-p'/q)=f(-1/z-1)=f(-1/z)$, so the
printed identity would say $f(z)=\omega_{1/1}(z/i)^{1/2}e^{\pi i/(12z)}e^{-\pi iz/12}f(-1/z)$, while
(24) says $f(z)=(z/i)^{1/2}e^{\pi i/(12z)}e^{+\pi iz/12}f(-1/z)$. Comparing the two gives
$\omega_{1/1}=e^{\pi iz/6}$ for every $z\in\HH$, which is not a constant. So the exponent printed
with a minus sign is a slip; Theorem 2 is the correct form and it reduces to (24) at $q=1$.

*(b) The variable.* The printed formula writes $z$ both in the argument $z-p/q$ of the left-hand
side and inside the prefactor $(zq/i)^{1/2}$ and the two exponentials. Since the left side is the
function $\xi\mapsto f(\xi+p/q)$ of the shifted variable $\xi=z-p/q$, the only reading consistent
with (24) is the one of Theorem 2: everything on the right is evaluated at the shifted variable, and
the statement is the local model of $f$ *at the point $p/q$*. (Read literally with the unshifted
$z$, the formula is false already for $q=1$ by (a).)

*(c) The order of the root of unity.* Theorem 2 gives $\omega_{p/q}\in\mu_{24q}$, because the factor
$e^{\pi i(p+p')/(12q)}$ in it is in general only a $24q$-th root of unity (for $q=3$, $p=p'=1$ it is
$e^{\pi i/18}$, of order $36$) and can be cancelled only by $\varepsilon(\gamma)$. So the book's
"appropriate $24$th root of unity" is a statement about the multiplier of $\eta$; it amounts to a
Dedekind-sum congruence, which the book neither states nor proves (the book has only the case
$\gamma=S$, Proposition 1.9 of Chapter 10). Nothing below uses more than $|\omega_{p/q}|=1$. (A
numerical evaluation of both sides of Theorem 2 for $p/q=1/3$ with principal branches gives an
$\omega_{1/3}$ of order $36$, hence not a $24$th root of unity; this is a check, not part of the
proof.)

## 2. What each factor contributes

Write the identity of Theorem 2 as a product of a local model and an error factor, in the shifted
variable $\xi$,
$$
f_{p/q}(\xi)=\omega_{p/q}\Bigl(\frac{\xi q}{i}\Bigr)^{1/2}
e^{\pi i/(12q^2\xi)}e^{\pi i\xi/12},
\qquad
f\Bigl(\xi+\frac pq\Bigr)=f_{p/q}(\xi)\,f\Bigl(-\frac{1}{q^2\xi}-\frac{p'}{q}\Bigr).
$$
The five factors do the following.

| factor | size at $\xi=x'+iy'$ | what it contributes |
|---|---|---|
| $\omega_{p/q}$ | $1$ | The transformation constant. It is a root of unity, so it influences no estimate; it enters the coefficient $c_{p/q}$ of the contribution, and in the exact formula it is part of the Hardy--Ramanujan sum. |
| $(\xi q/i)^{1/2}$ | $(q\lvert\xi\rvert)^{1/2}$ | The weight-$1/2$ (square-root) branch of $\eta$. It is the factor that supplies $q^{1/2}$ to the main term (the exponent below supplies $K/q$); in Theorem 3 it produces $\lvert c_{p/q}\rvert=\sqrt q$. |
| $e^{\pi i/(12q^2\xi)}$ | $e^{-\pi y'/(12q^2\lvert\xi\rvert^2)}$ | The essential singularity at $p/q$, which is $q^2$ times flatter than the one at $0$: the factor is $O(1)$ once $\lvert\xi\rvert\ge\sqrt{y'}/q$, and it blows up like $e^{\pi/(12q^2\lvert\xi\rvert)}$ as $\xi\to0$. This is what replaces $s$ by $s/q$ in the computation of §4, and hence turns $K$ into $K/q$ in the exponent of the main term. |
| $e^{\pi i\xi/12}$ | $e^{-\pi y'/12}$ | Together with the factor $e^{-2\pi in\xi}$ of (23) it gives $e^{-2\pi i(n-\frac1{24})\xi}$: this factor is exactly where the shift $n\mapsto n-\frac1{24}$ of Theorem 4.1 comes from (the book: "the fraction $1/12$ arising above will explain the occurrence of the fraction $1/24$"). |
| $f(-1/(q^2\xi)-p'/q)$ | $1+O\bigl(e^{-2\pi y'/(q^2\lvert\xi\rvert^2)}\bigr)$ | The error factor. Since $\operatorname{Im}\bigl(-1/(q^2\xi)\bigr)=y'/(q^2\lvert\xi\rvert^2)\to+\infty$ as $\xi\to0$, (25) gives $f=1+O(e^{-2\pi y'/(q^2\lvert\xi\rvert^2)})$; where $y'/(q^2\lvert\xi\rvert^2)\le1$ one uses instead $\lvert f\rvert\le Ce^{\pi/(12\,y'/(q^2\lvert\xi\rvert^2))}$, which follows from (24) exactly as the book's (28). These are the book's two estimates (27)--(28) with $\delta/(\delta^2+x^2)$ replaced by $y'/(q^2\lvert\xi\rvert^2)$. |

## 3. The contribution of the point $p/q$ to $p(n)$

**Theorem 3.** Fix $n\ge2$, put $\lambda=(n-\frac1{24})^{1/2}$, $\mu_q=(2\sqrt6\,q\lambda)^{-1}$ and
$s_q=\dfrac{\pi}{\sqrt6}\dfrac{\lambda}{q}=\dfrac{K\lambda}{2q}$. Let $A_{p/q}$ be an arc of
$\operatorname{Im}z=\delta$ about $p/q$ of length $\asymp1/(q n^{1/2})$ (a Farey arc of level
$\asymp n^{1/2}$), where $\delta=(4\sqrt6\,n^{1/2})^{-1}$ as in the book. Then the value that (23)
takes on $A_{p/q}$ once $f$ is replaced by $f_{p/q}$ — that is, the integral
$\displaystyle\int_{A_{p/q}}f_{p/q}(\xi)\,e^{-2\pi in(p/q+\xi)}\,d\xi$, in which $z=p/q+\xi$ — is
$$
c_{p/q}\,\frac{1}{2\pi\sqrt2}\,\frac{d}{dn}\left[\frac{e^{(K/q)\lambda}}{\lambda}\right]
\bigl(1+O(n^{-1/2})\bigr),
\qquad c_{p/q}=\sqrt q\;e^{-2\pi inp/q}\,\omega_{p/q},
$$
so that $|c_{p/q}|=\sqrt q$; for $p/q=0/1$ this is exactly the main term of Theorem 4.1(ii), where
$c_{0/1}=1$. (This is a statement about the local integral on one arc. It says nothing about the sum
over $p/q$, and it does not assert that replacing $f$ by $f_{p/q}$ on the other arcs is legitimate —
see section 4.)

*Proof.* On $A_{p/q}$ write $z=p/q+\xi$ and use
$f(z)=f_{p/q}(\xi)f(-1/(q^2\xi)-p'/q)$ of Theorem 2. There
$\operatorname{Im}\bigl(-1/(q^2\xi)-p'/q\bigr)=y'/(q^2|\xi|^2)\ge c\,n^{1/2}$ for a constant $c>0$,
because $y'=\delta\asymp n^{-1/2}$ and $|\xi|\le C/(qn^{1/2})$; so by (25) the second factor is
$1+O(e^{-c'n^{1/2}})$, and the discarded piece is smaller than any power of $n$.

*Step 1 (the $d/dn$ device of §4).* Using $d/dn\,e^{-2\pi in\xi}=-2\pi i\,\xi e^{-2\pi in\xi}$ and
$\xi\,(\xi/i)^{-1/2}=i\,(\xi/i)^{1/2}$,
$$
\int\Bigl(\frac{\xi}{i}\Bigr)^{1/2}e^{\pi i/(12q^2\xi)}e^{\pi i\xi/12}e^{-2\pi in\xi}d\xi
=\frac{1}{2\pi}\frac{d}{dn}\int\Bigl(\frac{\xi}{i}\Bigr)^{-1/2}
e^{\pi i/(12q^2\xi)}e^{\pi i\xi/12}e^{-2\pi in\xi}d\xi ,
$$
which is the book's identity $p_1(n)=\frac{d}{dn}q(n)+e(n)$, with $(z/i)^{1/2}$ replaced by
$(\xi q/i)^{1/2}=q^{1/2}(\xi/i)^{1/2}$; the factor $e^{-2\pi inp/q}$ coming from
$e^{-2\pi inz}=e^{-2\pi inp/q}e^{-2\pi in\xi}$ is constant for the $\xi$-integration and for the
$d/dn$ device, and is carried along. Hence the local contribution equals
$$
e^{-2\pi inp/q}\,\omega_{p/q}\,q^{1/2}\frac{1}{2\pi}\frac{d}{dn}
\int_{A_{p/q}}\Bigl(\frac{\xi}{i}\Bigr)^{-1/2}e^{\pi i/(12q^2\xi)}e^{\pi i\xi/12}e^{-2\pi in\xi}d\xi ,
$$
the term $e(n)$ produced by the variation of the arc being absorbed as in the book.

*Step 2 (rescaling).* Let $F(\zeta)=i(\zeta-1/\zeta)$ and $\xi=\mu_q\zeta$. Then
$$
\frac{\pi i}{12q^2\xi}-2\pi i\Bigl(n-\frac1{24}\Bigr)\xi
=\frac{s_q i}{\zeta}-s_q i\zeta=-s_qF(\zeta),
$$
the two conditions being $s_q=\pi/(12q^2\mu_q)$ and $s_q=2\pi\mu_q(n-\frac1{24})$, i.e.
$\mu_q^2=\bigl(24q^2(n-\frac1{24})\bigr)^{-1}$ and then $s_q=(\pi/\sqrt6)\lambda/q$. This is the
book's change of variables $z\mapsto\mu z$ with $(A,\mu)$ replaced by $(s_q,\mu_q)$; note that
$s_q=s/q$ and $\mu_q=\mu/q$ in the notation of §4, that
$(\xi/i)^{-1/2}d\xi=\mu_q^{1/2}(\zeta/i)^{-1/2}d\zeta$, and that $|\xi|\le C/(qn^{1/2})$ becomes
$|\zeta|\le C'$: the arc reaches far beyond the width $s_q^{-1/2}\asymp(q/n^{1/2})^{1/2}$ of the
Gaussian at the saddle, which is what the method needs (for fixed $q$ that width tends to $0$).

*Step 3 (Laplace's method).* $F=i(\zeta-1/\zeta)$ has its only critical point at $\zeta=i$, with
$F(i)=-2$ and $F''(i)=2$, and the book's contour $\Gamma^*$ (the segments $[\pm a_n,\pm1]$ and the
upper unit semicircle) is admissible for $F$. On the semicircle $\zeta=e^{i\theta}$, with $\theta$
running from $\pi$ to $0$, one has $F=-2\sin\theta$ and
$(\zeta/i)^{-1/2}d\zeta=e^{3\pi i/4}e^{i\theta/2}d\theta$, so after $\theta=\frac\pi2+\varphi$ the
semicircle contributes
$$
\int_{-\pi/2}^{\pi/2}e^{2s_q\cos\varphi}e^{i\varphi/2}d\varphi
=e^{2s_q}\sqrt{\frac{\pi}{s_q}}\bigl(1+O(s_q^{-1})\bigr):
$$
the sine part vanishes by oddness, and the cosine part has amplitude $1$ at the saddle $\varphi=0$, so
Laplace's method (Proposition 2.1, applied exactly as in §4 with $\Phi=-\cos$ and $\psi=1$) gives
the displayed Gaussian value. On the two real segments $F$ is purely imaginary, so the integrand has
modulus $|\zeta|^{-1/2}\le1$ there and their total contribution is $O(a_n)=O(q\lambda)$, where
$a_n=\mu_q^{-1}/2=\sqrt6\,q\lambda$; this is negligible compared with $e^{2s_q}$ for fixed $q$ as
$n\to\infty$. (This is the book's $O(a_n\mu^{3/2})=O(1)$, with the extra $q^{1/2}$ of the prefactor;
see section 4.)

*Step 4 (the constant).* By Step 3, the integral appearing in Step 1 equals
$$
\mu_q^{1/2}\,e^{2s_q}\sqrt{\frac{\pi}{s_q}}\bigl(1+O(s_q^{-1})\bigr)
=\frac{1}{\sqrt2}\,\lambda^{-1}e^{K\lambda/q}\bigl(1+O(n^{-1/2})\bigr),
$$
because, with $\mu_q^{1/2}=(2\sqrt6\,q\lambda)^{-1/2}$ and $s_q^{-1/2}=(2q/(K\lambda))^{1/2}$,
$$
\mu_q^{1/2}\sqrt{\frac{\pi}{s_q}}
=(2\sqrt6)^{-1/2}\sqrt{\frac{2\pi}{K}}\;\lambda^{-1}=\frac{1}{\sqrt2}\,\lambda^{-1}:
$$
the powers of $q$ cancel, and
$(2\sqrt6)^{-1/2}\sqrt{2\pi/K}=\sqrt{\pi/(K\sqrt6)}=1/\sqrt2$ because
$K\sqrt6=\pi\sqrt{2/3}\sqrt6=2\pi$. Substituting into Step 1 and using
$\frac{1}{2\pi}\cdot\frac{1}{\sqrt2}=\frac{1}{2\pi\sqrt2}$, the local contribution is
$$
e^{-2\pi inp/q}\,\omega_{p/q}\,\frac{1}{2\pi\sqrt2}\,q^{1/2}
\frac{d}{dn}\Bigl[\frac{e^{(K/q)\lambda}}{\lambda}\Bigr]\bigl(1+O(n^{-1/2})\bigr)
=c_{p/q}\,\frac{1}{2\pi\sqrt2}\,\frac{d}{dn}\Bigl[\frac{e^{(K/q)\lambda}}{\lambda}\Bigr]
\bigl(1+O(n^{-1/2})\bigr),
$$
with $c_{p/q}=\sqrt q\,e^{-2\pi inp/q}\omega_{p/q}$, which is the assertion. Equivalently,
carrying out the $\xi$-integration of the model directly (without the $d/dn$ device) gives
$\omega_{p/q}\frac{1}{4\sqrt3}q^{-1/2}\lambda^{-2}e^{K\lambda/q}$, which is the same number, since
$\frac{1}{2\pi\sqrt2}\frac{K}{2}=\frac{K}{4\pi\sqrt2}=\frac{1}{4\sqrt3}$. For $q=1$, $p=0$ we have
$\omega_{0/1}=1$ and
$\frac{1}{2\pi\sqrt2}\frac{K}{2}\lambda^{-2}e^{K\lambda}=\frac{1}{4\sqrt3}\lambda^{-2}e^{K\lambda}$
because $K/(4\pi\sqrt2)=\sqrt{2/3}/(4\sqrt2)=1/(4\sqrt3)$;
with $\lambda^2=n+O(1)$ this is $\sim e^{Kn^{1/2}}/(4n\sqrt3)$, which is Theorem 4.1(i). $\square$

Two consequences worth recording, since they are the bookkeeping the exercise asks for.

* The $q$-dependence is exactly what the exercise prints: the exponent $K\lambda$ of the case $q=1$
  becomes $K\lambda/q$, and in the derivative form no other power of $q$ survives except the
  $\sqrt q$ inside $c_{p/q}$. In the undifferentiated form, i.e. for $p_1(n)$ rather than
  $\frac{d}{dn}q(n)$, the same computation gives
  $\frac{1}{4\sqrt3}q^{-1/2}\lambda^{-2}e^{K\lambda/q}$; the two forms agree because
  $\frac{d}{dn}[\lambda^{-1}e^{K\lambda/q}]=\frac{K}{2q}\lambda^{-2}e^{K\lambda/q}(1+O(n^{-1}))$
  and $\frac{1}{4\sqrt3}\Big/\frac{K}{2}=\frac{1}{2\sqrt3 K}=\frac{1}{2\pi\sqrt2}$, the last
  equality being $\sqrt3 K=\sqrt3\pi\sqrt{2/3}=\pi\sqrt2$.
* For $q\ge2$ the local term is smaller than the term $q=1$ by the factor
  $e^{-K\lambda(1-1/q)}$, so the series over $q$ is dominated by $q=1$; and for fixed $n$ the sum of
  $c_{p/q}/\sqrt q$ over $p$ with $(p,q)=1$ is $\sum_p e^{-2\pi inp/q}\omega_{p/q}$, the
  Hardy--Ramanujan sum.

## 4. What the book does not carry out, and what is therefore not proved here

The exercise's last sentence — that the series over all proper fractions $p/q$, "when suitably
modified", converges and gives an **exact** formula for $p(n)$ — is not proved in the book, and it is
not proved above. What is missing is the following, and each item is needed for that sentence.

1. **The multiplier $\varepsilon(\gamma)$ (Lemma 1) is not in the book.** The book has only
   $\eta(-1/z)=(z/i)^{1/2}\eta(z)$ (Chapter 10, Proposition 1.9), i.e. the case $\gamma=S$. The
   general case is the classical Dedekind-sum formula for $\varepsilon(\gamma)$; Lemma 1 above
   proves existence and $\varepsilon(\gamma)\in\mu_{24}$ but gives no closed form. In particular the
   book's $\omega_{p/q}$ is never determined: see Remark 3(c).
2. **The passage from the one singularity $z=0$ to all of them.** The book's §4 does the whole
   computation for $z=0$ alone, on the single contour $\gamma'$: it replaces $f$ by $f_1=f_{0/1}$ on
   the *whole* segment and controls the difference with (26)--(28). For $p/q\ne0$ that replacement
   is not legitimate on the whole segment, since the width of the region where $f_{p/q}$ is an
   admissible model is only $\asymp\sqrt{y}/q$ (third row of the table). One needs: (a) a dissection
   of the line $\operatorname{Im}z=\delta$ into one arc $A_{p/q}$ for each fraction $p/q$ with
   $q\le N$; (b) on each arc an estimate of $|f/f_{p/q}-1|$ uniform in $p$; (c) a choice of $N$ and
   $\delta$ as functions of $n$; (d) an estimate for the sum over all $p/q$ with $q\le N$ of the
   remaining pieces (the radial segments), and for the tail $q>N$. The book does none of (a)--(d);
   it says only "when suitably modified".
3. **The book's own error term is too coarse to see the terms $q\ge2$.** With the book's
   $\delta=(4\sqrt6\,n^{1/2})^{-1}$, the estimates (26)--(28) give the error
   $O(e^{2\pi n\delta}e^{\pi/(48\delta)})=O(e^{Kn^{1/2}/2})$ (in the second regime one uses
   $q^2(\delta^2+x'^2)\le q^2\delta^2+\tfrac14$ with $|x'|\le1/(2q)$, so $1/Y\le q^2\delta+1/(4\delta)$,
   which is $\le C/\delta$ for an absolute $C$).
   But the local term at $p/q$ is only $e^{K\lambda/q}$, so for every $q\ge2$ it is at most of the
   order of the book's error term. Hence the book's estimates cannot exhibit *any* of the
   contributions $q\ge2$ that the exercise asserts. Finer arcs and a finer choice of $\delta$
   (item 2) are indispensable.
4. **Convergence of the modified series and the exact formula.** Even granting (a)--(d), the terms
   carry relative error factors $1+O(n^{-1/2})$, and $e^{-2\pi inp/q}\omega_{p/q}$ is not constant in
   $n$; so the displayed shape
   "$c_{p/q}\cdot\frac{1}{2\pi\sqrt2}\frac{d}{dn}[\cdot]$" is not an identity of functions of $n$
   for $q\ge2$, and the coefficient has to be taken at the given $n$ — this is why the exact formula
   has a coefficient $A_q(n)$ depending on $n$ (the Hardy--Ramanujan sum of the bookkeeping above)
   rather than a constant $c_{p/q}$. Making the sum over $p/q$ converge and equal $p(n)$ needs the
   refinement of Rademacher (1937): the modified dissection with level $N\asymp n^{1/2}$, the
   resulting error bound uniform in $p$, and the choice of $\delta$ adapted to the arc. None of this
   is in the book.

So: the transformation law is proved (Theorem 2, with the corrections of Remark 3), and the local
contribution of each rational point is proved (Theorem 3, with $|c_{p/q}|=\sqrt q$ and the constant
$1/(2\pi\sqrt2)$, both checked by reduction to Theorem 4.1(ii) at $q=1$). The exact formula itself is
asserted by the book without proof, and items 1--4 above are what a proof would still have to
supply.

:::
