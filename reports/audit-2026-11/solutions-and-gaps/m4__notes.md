# Slice 3 — Stein–Shakarchi, Appendix A §5, Problems 1 and 2

Deliverables (each is the complete `::: {.solution}` block, ready to append to the card):

- `E-SSA.PR-1.solution.md` — card `corpus/collections/SRC-TEXT-SS03/appendix-a-problems/E-SSA.PR-1.md`
  (Watson's lemma for a truncated integral with a smooth cutoff, parts (a) and (b)).
- `E-SSA.PR-2.solution.md` — card `E-SSA.PR-2.md`
  (Stirling with the asymptotic expansion in powers of $s^{-1}$, for $s\in S_\delta$).

Source quoted: `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`, Appendix A, §5 Problems,
printed pp. 341–343 (= PDF pp. 360–362); §1–§2 printed pp. 319–328 (= PDF pp. 338–347);
Chapter 6 Lemma 1.2 / Theorem 1.4, printed pp. 161, 164.

## What is proved

PR-1. Both parts, with the book's own strategy.
The one tool is a cut-off lemma: for $g\in C^\infty([0,\infty))$ vanishing identically on $[0,a)$ and on
$(b,\infty)$, $n$ integrations by parts with all boundary terms zero give
$|\int_0^\infty e^{-sx}g|=O(|s|^{-n})$ uniformly for $\Re s\ge0$.
(a) $D(s)=\int e^{-sx}x^m\eta-s^{-m-1}\Gamma(m+1)$ equals $-\int e^{-sx}x^m(1-\eta)$ on $\Re s>0$
(the substitution $x=t/s$) and both sides are holomorphic on the slit plane, so the identity extends to
$\Re s\ge0$; the cut-off lemma applies to $x^m(1-\eta)$, which is $C^\infty_c$ and vanishes near $0$.
(b) $k=\lceil m\rceil$ (with $k=0$ allowed exactly when $m\le0$), $(x^m)^{(k)}=c\,x^{m-k}$ with
$m-k\in(-1,0]$, part (a) applied to $m-k$, then $k$ integrations by parts; the intermediate
$G_i=\int e^{-sx}(x^m)^{(i)}\eta'$ are $O(|s|^{-n})$ for every $n$ because $(x^m)^{(i)}\eta'$ is
$C^\infty_c$ vanishing near $0$. Finally $c\Gamma(m-k+1)=\Gamma(m+1)$ by Lemma 1.2 of Chapter 6.
The vanishing of the boundary terms uses $m-k+1>0$, which is where the constraint $k-1<m$ is spent.

PR-2. The full expansion, uniformly on $S_\delta$, with $a_j=\alpha_{2j}(2j-1)!!$ and $a_1=1/12$.
1. $\Gamma(s)=e^{s\log s-s}\int_0^\infty e^{-s\Phi}dx/x$, $\Phi(x)=x-1-\log x$ (book, p. 326).
2. Exact quadratic substitution near $x=1$: $v=(x-1)\sqrt{h(x-1)}$, $\Phi=v^2/2$, $dx/x=A(v)dv$,
   $A=v/(x(v)-1)$, $A(0)=1$; $A=1-v/3+v^2/12+\dots$ so $\alpha_1=-1/3$, $\alpha_2=1/12$ (hand-checkable
   series reversion, independently confirmed with exact rational arithmetic).
3. Watson-with-cutoff lemma (the "Problem 1 in place of Proposition 1.3" input): for $A$ holomorphic on
   $|v|<2\rho$ and $\chi\equiv1$ on $[-\rho,\rho]$, $\int_{\mathbb R}e^{-sv^2/2}A\chi
   =\sum_{k\le K}\alpha_{2k}(2k-1)!!\sqrt{2\pi}s^{-k-1/2}+O(|s|^{-K-1})$. Proved by exact Gaussian
   moments plus $K+1$ boundary-free integrations by parts against the quadratic phase.
4. The complementary piece $\int e^{-s\Phi}(1-\eta)dx/x$ is $O(|s|^{-M})$ for every $M$ and
   $\Re s\ge1/2$, by the book's device $e^{-s\Phi}=-(1/s)(e^{-s\Phi})'/\Phi'$ iterated (amplitude
   $\psi/\Phi'=(1-\eta)/(x-1)$ smooth; boundary terms vanish at $0$, $1$ and $\infty$).
5. Hence on $\Re s\ge1/2$: $F(s)=\Psi_N(1/s)+O(|s|^{-N-1})$ for $F=\sqrt{s/2\pi}\,\Gamma e^{-s\log s+s}$.
6. Recurrence $F(s)=E(s)F(s+1)$, $E=e^{(s+1)\log(1+1/s)-1}(1+1/s)^{-1/2}$, extends it to $\Re s\ge0$
   with the same coefficients (uniqueness of asymptotic coefficients on the overlap $\Re s\ge1/2$).
   This step is what reaches the imaginary axis, where no contour deformation can help.
7. Exact identity $F(s)F(-s)=1/(1-e^{2\pi is})$ for $\Im s>0$ and $1/(1-e^{-2\pi is})$ for $\Im s<0$
   (from $\Gamma(s)\Gamma(-s)=\pi/(-s\sin\pi s)$, the book's (14)).
8. Hence for $\Re s<0$ in $S_\delta$: $F(s)=1/\Psi_N(-1/s)+O(|s|^{-N})$.
9. Coefficient identification: comparing the two expansions on the imaginary axis gives the formal
   identity $\Psi_N(u)\Psi_N(-u)=1+O(u^{N+1})$, so the left-half-plane expansion is again
   $\Psi_N(1/s)+O(|s|^{-N})$; the sector is covered.

## Verification performed

- $\alpha_2=1/12$ and the Stirling coefficients $1,1/12,1/288,-139/51840,-571/2488320,\dots$ computed
  exactly by formal series reversion (rational arithmetic), matching the classical values.
- Numerically (mpmath, 40–60 digits): the substitution identity $\Gamma(s)=\sqrt{2\pi}\,e^{s\log s-s}
  \int_{\mathbb R}e^{-|s|\rho^2/2}A(e^{i\varphi}\rho)d\rho$; the expansion with remainder
  $O(|s|^{-N})$ at $s=20,\ 20i,\ 14.14+14.14i,\ -10+17i$; the recurrence factor $E(s)$; the reflection
  identity in both half-planes; and the statement of PR-1 for several $m$ (including $m=3.7$ and
  $m=-1/2$) on the imaginary axis.
- Markup: both blocks run through `pandoc --lua-filter ~/.pandoc/filters/lamport_proof.lua` with no
  warnings, every `pf-ref` resolving to its step number, one QED per proof.

## Honest notes

- The book's hint for Problem 2 ("use Problem 1 in place of Proposition 1.3") governs only the local
  Laplace analysis. Taken literally it is not enough: with a fixed cut-off in $x$, the complementary
  integral is only $O(1/|s|)$ when $\Re s$ is small (this is why Theorem 2.3 gets $O(|s|^{-1/2})$
  relative error and no better), so the arbitrary-order statement on the closed half-plane needs both
  (i) the exact quadratic substitution plus the cut-off Watson lemma for the local piece and
  (ii) the recurrence $s\mapsto s+1$ to reach the imaginary axis. Nothing in the solution is weakened,
  and no step is left to the reader as "standard".
- The solution does not use Binet's formula or Euler–Maclaurin; both are absent from this book, and the
  proof above stays within Appendix A plus Chapter 6's Lemma 1.2 and Theorem 1.4.
