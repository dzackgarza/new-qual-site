---
schema: qual/card@1
id: P-CEZOG
kind: problem
title: "If $A$ is a cyclic module over a commutative ring $R$, so we have $A =\u2026"
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---
If $A$ is a cyclic module over a commutative ring $R$, so we have $A = Ra$ for some $a\in A$. By Hungerford's definition, the submodule $A$ has order $r$ $\iff$ the element $a$ has order $r$ $\iff$ the order ideal $\mathcal{O}_a \definedas \theset{x\in R \mid xa = 0} = (r)$. 

In particular, $ra = 0$.

### Part 1

Since $(r, s) = (1)$, we can find $t_1, t_2 \in R$ such that
\[
\begin{align*}
t_1r + t_2 s = 1 &\implies t_1ra + t_2 sa = 1a  &\\
&\implies t_1(ra) + t_2 sa = a &\\
&\implies t_2 sa = a &\text{since $ra=0$}\\
&\implies s(t_2 a) = a &\text{since $R$ is commutative}
,\end{align*}
\]

which implies that $a \in sA$ and thus $A \subseteq sA$. However, we always have $sA \subseteq A$ for modules, so this shows that $A = sA$.

To see that $A[s] = \theset{x\in A \mid sx = 0} = 0$, let $x\in A[s]$; we will show $x=0$. Since $x\in A = Ra$, we have $x = r_1 a$, and in particular 
$$
ra = 0 \implies rx = r r_1 a = r_1 (ra) = 0.
$$

So we now have $rx = 0$ and $sx=0$, and we can write
\[
\begin{align*}
x &= (t_1 r + t_2 s)x \\
&= t_1 (rx) + t_2 (sx) \\
&= t_1 0 + t_2 0 \\
&= 0
.\end{align*}
\]

So $x = 0$ and thus $A[s] = 0$.
$\qed$

### Part 2

Suppose $r = sk$. 
Toward an application of the first isomorphism theorem, define a map
\[
\begin{align*}
\phi: R &\to sA = sRa \\
x &\mapsto sxa
.\end{align*}
\]

**$\phi$ is well-defined**: 

This follows from that fact that $a\in A \implies xA \in A$ for any $x\in R$, so the codomain is in fact $sA$. 

**$\phi$ is an $R\dash$module homomorphism:** 

We have 
\[
\begin{align*}
t\in R \implies \phi(tx) &= s(tx)a = t(sxa) = t\phi(x) \\
x,y \in R \implies \phi(x + y) &= s(x+y)a = sxa + sya + \phi(x) + \phi(y)
\end{align*}
\]


**$\ker \phi = (k)$**: 

Suppose $x\in \ker\phi$ so $sxa = 0_A$; we'd like to show $x \in (k)$.

By definition $sx \in \mathcal O_a$, and by assumption $\mathcal O_a = (r)$, so $sx = t_1 r$ for some $t_1 \in R$. 
\[
\begin{align*}
& sxa = 0_A \\
\implies sx &= t_1 r &\text{since $sx \in \mathcal O_a$} \\
\implies sx &= t_1 (sk)  &\text{since $r=sk$ by assumption}\\
\implies sx &= s (t_1 k) &\text{since elements in $R$ and $A$ commute}\\
\implies x &= t_1 k &\text{since $R$ is a domain, so $sm = sn, s\neq 0 \implies m=n$}
,\end{align*}
\]

which exhibits $x = t_1 k \implies x\in (k)$ as desired.

**$\phi$ is surjective:**

Since $A=Ra$, we have $sA =sRA$ and thus $x\in sA \implies x = sra$ for some $r\in R$; but then $\phi(r) = sra = x$.

We thus have
\[
\begin{align*}
R/\ker \phi \cong \im \phi \implies R/(k) \cong sA.
\end{align*}
\]


Similarly, define a map
\[
\begin{align*}
\psi: R &\to A[s] \\
x &\mapsto kxa
\end{align*}
\]

**$\psi$ is well-defined**:

It suffices to check that $\im \psi \subseteq A[s]$ (since we will show surjectivity shortly), i.e. that $s$ annihilates anything in the image. This follows from
$$
s (kxa) = (sk)xa = rxa = x(ra) = 0,
$$
since $ra = 0$ by assumption.


**$\psi$ is an $R\dash$module homomorphism:**

We can check
$$
\psi(tr_1 + r_2) = k(tr_1 + r_2)s = tkr_1s + kr_2 s = t\psi(r_1) + \psi(r_2)
$$

which follows because elements of $R$ commute with those from $A$ under multiplication.

**$\ker \psi = (s)$**:

Suppose $x\in \ker\psi$, so $kxa = 0$. Then $kx \in \mathcal O_a = (r)$, so $kx = r t_1$. Then

\[
\begin{align*}
& kxa = 0_A  \\
&\implies kx = r t_1 & \text{since } kx \in \mathcal O_a\\
&\implies kx = (sk)t_1  &\text{since } r = sk\\
&\implies kx = k(st_1) &\text{since $R$ is commutative} \\
&\implies x = s t_1 &\text{since $R$ is a domain},
\end{align*}
\]
and so $x\in (s)$ as desired.

**$\psi$ is surjective:**

Letting $y \in A[s]$ be arbitrary. We have
\[
\begin{align*}
y \in A[s] &\implies x = t_1 a,\quad sx = 0 \\
&\implies s(t_1 a) = 0 \\
&\implies st_1 \in \mathcal O_a \implies \exists x\in R \suchthat st_1 = xr = x (sk) \\
&\implies st_1 = sxk \\
&\implies t_1 = xk \qquad\qquad\text{since $R$ is a domain} \\
&\implies y = t_1 a = (x k)a = kxa, 
\end{align*}
\]

so $\psi(x) = y$.

We can then apply the first isomorphism theorem
$$
R/\ker \psi \cong \im \psi \implies R/(s) \cong A[s].
$$

$\qed$

