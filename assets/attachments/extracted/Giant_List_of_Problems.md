## Real Analysis Questions

## October 2012

## Contents

1 Measure Theory 1   
2 Riemann Integration 3   
3 Lebesgue Integration 3   
4 Fourier Transform and Fourier Series 4   
5 Functional Analysis 6   
6 $L ^ { p }$ Spaces 7   
7 Convolution 8   
8 Different Kinds of Convergence 8   
9 Differentiation 9   
10 Absolute Continuity and Bounded Variation 10   
11 Lebesgue Differentiation Theorem 11   
12 Category, Completeness, Continuity, and Convexity 11   
13 Probability 12   
14 Differential Equations 12   
15 Harmonic Functions 13   
16 Asymptotics 13   
17 Sequences and Series 13   
18 Diophantine Problems 14

## 1 Measure Theory

Question 1.1. What is a measurable function? Is the composition of two measurable functions measurable?

Question 1.2. What is the measure of a set on the real line? When is a set measurable? Name some measurable sets. What are the operations that you can do to measurable sets to get measurable sets?

Question 1.3. Are all subsets of R measurable? Give me a nonmeasurable subset.

Question 1.4. What is the measure of a countable set? Can an uncountable set have zero measure?

Question 1.5. Are there any Borel sets besides $F _ { \sigma }$ and $G _ { \delta }$ sets?

Question 1.6. Do the rational numbers form a $G _ { \delta }$ set?

Question 1.7. Construct a measurable set that is not Borel. Why are there more Lebesgue measurable sets than Borel?

Question 1.8. What is the completion of a measure?

Question 1.9. State/prove the Riesz representation theorem. What about noncompact sets? Could you give an example of a positive linear functional on continuous functions on the real line which is not given by a measure?

Question 1.10. State the Radon–Nikodym theorem. How does this give a Lebesgue analogue of the fundamental theorem of calculus?

Question 1.11. How can you associate a measure to a monotonically increasing function which is bounded?

Question 1.12. Give an example of a singular measure (with respect to Lebesgue). Look at the distribution function. What can you say? Can you give a singular measure that has a continuous distribution function? Define absolute continuity of a measure (with respect to another measure).

Question 1.13. Give an example of mutually singular measures on the real line that both assign positive measure to all intervals.

Question 1.14. Let E be a measurable set in R with positive measure. Do there necessarily exist distinct points x,y in E whose average $( x + y ) / 2$ is in E?

Question 1.15. Suppose E has positive Lebesgue measure. Prove that the set $E - E$ of differences of elements of E contains an interval.

Question 1.16. Show that if E is measurable and has positive measure, then E +E contains an interval.

Question 1.17. Suppose we are given a group homomorphism from the reals to the reals.   
Show that if it is measurable then it is linear.

Question 1.18. Define Hausdorff dimension.

Question 1.19. What is the Hausdorff dimension of the Cantor set?

Question 1.20. What is the measure of the Cantor set? What can you say about Cantor sets in general? Does a Cantor set always have measure zero? What happens if you take a middle fifths set instead of a middle thirds set?

Question 1.21. If the Cantor set is homeomorphic to another subset $o f \mathbb { R }$ , does that set also have measure 0?

Question 1.22. Construct a variant of the Cantor set that has positive measure.

Question 1.23. Can you find an open dense subset of [0, 1] with measure $1 / 2 \ell$

Question 1.24. If $E _ { n }$ are measurable sets in [0, 1], and $m ( E _ { n } ) \to 1$ as $n  \infty$ , what can you say about the measure of their intersection?

Question 1.25. Let $E _ { n }$ be a sequence of measurable sets in [0, 1] with $m ( E _ { n } )  1$ as $n \to \infty$ Does there exist a subsequence whose intersections all have measure greater than $1 / 2 \ell$

Question 1.26. $I f \sum m ( E _ { n } )$ is finite, show that the set of points lying in infinitely many of the $E _ { n }$ has measure 0.

Question 1.27. Suppose you had a sequence of sets $E _ { n } \subset E$ where E has finite measure and $m ( E _ { n } ) \geq 1 / 2$ . What can you say about the set of x which lie in infinitely many of the $E _ { n } ! ~ \ell$

Question 1.28. What is weak convergence of measures?

Question 1.29. Suppose I have a sequence of measures $\mu _ { k }$ , say, on $\mathbb { R } ^ { n }$ , that converges weakly to some limiting measure µ. For what closed sets C in $\mathbb { R } ^ { n }$ do I have $\mu _ { k } ( C ) \to \mu ( C ) \mathop { ? }$

## 2 Riemann Integration

Question 2.1. Why is Lebesgue integration so much better than Riemann integration?

Question 2.2. What is a necessary and sufficient condition for a function to be Riemann integrable?

Question 2.3. Is it possible that the characteristic function of an open set is not Riemann integrable?

Question 2.4. Can you give an example of a dense open set in [0, 1] whose characteristic function is not Riemann integrable?

Question 2.5. Give an example of something that is Lebesgue integrable but not Riemann integrable.

Question 2.6. Do the Riemann integrable functions form a vector space? Is it complete with the “Riemann L1 norm”?

Question 2.7. Can you construct a measurable set on the interval [0, 1] such that its intersection with any subinterval of [0, 1] has measure neither 0 nor equal to the measure of the whole subinterval? If so, is the indicator (characteristic) function of that set Riemann integrable?

## 3 Lebesgue Integration

Question 3.1. What is the integral of a function?

Question 3.2. What are simple functions?

Question 3.3. What is Fatou’s lemma? Give an example where inequality holds strictly and a counterexample when you don’t assume the functions are nonnegative. Discuss the relation with the monotone and dominated convergence theorems.

Question 3.4. Given a sequence of functions converging pointwise, when does the limit of their integrals converge to the integral of their limit?

Question 3.5. State the monotone convergence theorem.

Question 3.6. State the dominated convergence theorem and Fubini’s theorem.

Question 3.7. Use Fubini’s theorem to compute the Gaussian integral.

Question 3.8. Given f in L1 over a space X and  > 0, can you find δ such that $\mu ( E ) < \delta$ implies $\textstyle \int _ { E } | f | d \mu < \epsilon ?$

Question 3.9. Given $f \in L ^ { 1 }$ , what can you say about $\textstyle F ( x ) = \int _ { a } ^ { x } f ( t ) d t ?$

Question 3.10. Is the indefinite integral of a function in L2(R) continuous? Prove it.

Question 3.11. If you have a function on a measure space of total measure 1 with L1 norm also equal to 1, what can you say about the measure of the set where it is greater than 10 000?

Question 3.12. If we integrate from 0 to 10, for what p is xp integrable? What about xp cos(1/x)? Does it matter whether we use the Lebesgue or the Riemann integral?

Question 3.13. For which (real) values of s is the integral over R of sin x/xs finite?

Question 3.14. If f is continuous and $\textstyle \int _ { 1 } ^ { \infty } f ( x ) x ^ { n } d x = 0$ for all $n \geq 2$ , what can you say about f?

## 4 Fourier Transform and Fourier Series

Question 4.1. What is the Fourier series of a function in L1(T), where T is the unit circle? Exhibit some statements about the relation between C(T) and Lp(T) to prove the Riemann– Lebesgue lemma.

Question 4.2. Say I have a Ck function on the circle. What can I say about the decay of its Fourier coefficients?

Question 4.3. What can you say about the Fourier coefficients of a Lipschitz function?

Question 4.4. Suppose that f is a continuous function on [0, 1] and that f is differentiable at 0. Show that the Fourier series for f converges at 0.

Question 4.5. Prove that the Fourier series of a smooth function converges to it everywhere.

Question 4.6. Take the characteristic function of an interval. Does the Fourier series converge absolutely? In what sense does it converge?

Question 4.7. Does the Fourier series of a continuous function on the circle converge to it pointwise? Prove there exist plenty of counterexamples using the uniform boundedness principle (also known as the Banach–Steinhaus theorem).

Question 4.8. What do you know about convergence of Fourier series? Ces\`aro summability? Dirichlet kernel? When is convergence uniform?

Question 4.9. What do you know about Fourier series? What can you say about decay of Fourier coefficients? How do you prove this? What conditions on the function would ensure rapid decay of the Fourier coefficients?

Question 4.10. What can you say about the Fourier series of a smooth function f? Conversely, does this condition imply that f is smooth?

Question 4.11. State/prove the Poisson summation formula.

Question 4.12. What is the Fourier transform (on the real line)?

Question 4.13. What can you say about the Fourier transform of an L1 function? Is this transform defined almost everywhere or everywhere? Is it continuous? Prove it. What did you use there? What is dominating what?

Question 4.14. State/prove the Riemann–Lebesgue lemma.

Question 4.15. Give some heuristic reasons why the Riemann–Lebesgue lemma should be true, the kind that engineers could understand.

Question 4.16. Is the image of the Fourier transform on L1(R) all of $C _ { 0 } ( \mathbb { R } ) \ell$

Question 4.17. The Fourier transform of an L1 function is continuous, but does it have to be differentiable? What if the function has compact support?

Question 4.18. State/prove Plancherel’s theorem.

Question 4.19. Do you know anything about Fourier analysis on Lp?

Question 4.20. What does “rapidly decaying” mean? If a function is smooth and rapidly decaying, what can you say about its Fourier transform?

Question 4.21. Define Schwartz space. What is the dual of the Schwartz space?

Question 4.22. Why does smoothness of a function imply decay of its Fourier transform?

Question 4.23. What is the relationship between the Fourier transform and convolution?

Question 4.24. Compute the Fourier transform of 1/(1 + x2).

Question 4.25. Compute the Fourier transform of sin x/x.

Question 4.26. Compute the Fourier transform of (sin x/x)2.

Question 4.27. What is the transform of the indicator (that is, characteristic) function of an interval?

Question 4.28. What is the Fourier transform of the Cantor–Lebesgue function? What is the Fourier transform of the Lebesgue–Stieltjes measure determined by the Cantor–Lebesgue function? Observe that it takes the same non-zero value at all the powers of 3, and conclude that the Fourier transform of a Borel measure does not necessarily tend to 0 at infinity (unlike the Fourier transform of an L1 function).

Question 4.29. What can you say about real-valued functions with positive-definite Fourier transform?

Question 4.30. What can you say about the Fourier transform of e−|x|3? Is the function in the Schwartz class? Why not? Is its transform in the Schwartz class? Why is e−|x|4 easier?

Question 4.31. Suppose you had a C∞ function with compact support. What can you say about its Fourier transform? Does it extend to an analytic function? What can you say about the rate of growth of this analytic function?

Question 4.32. What can you say about the Fourier transform of a radially symmetric function? Prove it is radially symmetric. Do you know what Bessel functions are?

Question 4.33. Suppose f is a function in L1(R). Define g(x) = RR f (t) cos(xt) dt. What can you say about g? Why is the integral finite for all x? Now prove that g is continuous.

Question 4.34. Take f in L1(R). Let $\begin{array} { r } { g ( y ) = \int _ { \mathbb { R } } \exp ( - i y x ^ { 2 } ) f ( x ) } \end{array}$ dx (so not the Fourier transform). What can you say about it? Existence? Continuity? Does it tend to 0 as y tends to infinity? Is it enough to prove the theorem for a dense subset of L1?

Question 4.35. What can you say about $\begin{array} { r } { \int _ { \mathbb { R } } f ( x ) \exp ( i \lambda g ( x ) ) } \end{array}$ dx. Examine the behaviour of nice functions under this. What if g0(x) vanishes, say polynomially, at just one point?

Question 4.36. Define $\begin{array} { r } { F ( s ) = \int _ { 0 } ^ { \infty } f ( x ) e ^ { - s x } } \end{array}$ dx, where f is “nice” (say smooth with compact support, and you may take that support to be bounded away from 0). Assume first that s is real. Is F always defined? Is it continuous? Differentiable? What is its derivative? What about when s is complex? When is F analytic? If s is purely imaginary, how do you recover f from F ? What does this tell you about the general case? What can you say about the Laplace transform of a function with bounded derivatives?

Question 4.37. Why are L1, L2, and L∞ estimates usually the “easiest” estimates. Why is an additive group necessary for doing Fourier analysis? How is Fourier analysis on a circle or higher-dimensional torus Tn different from Fourier analysis on Euclidean space $\mathbb { R } ^ { n } { \boldsymbol { \ell } }$

Question 4.38. What is the Hilbert transform, and what can you say about it?

## 5 Functional Analysis

Question 5.1. What is a Banach space? What is Lp? What is L1? What is a Hilbert space?

Question 5.2. Give us two Hilbert spaces which aren’t isomorphic in an obvious way but are isomorphic nevertheless!

Question 5.3. What do you mean by a basis for Hilbert space?

Question 5.4. Prove that a compact convex set in a Hilbert space has a unique element of minimal norm. What if it’s just closed and bounded instead of compact?

Question 5.5. What’s a compact linear operator? Is it possible to find a bounded operator without an eigenvector? What about a compact operator?

Question 5.6. What is the completion of the normed space consisting of continuous functions on [0, 1] with the sup norm? What about the norm given by integrating the absolute value?

Question 5.7. What’s the dual space of $C [ 0 , 1 ] ?$

Question 5.8. What is the Stone–Weierstrass theorem?

Question 5.9. What is a distribution?

Question 5.10. Let $\phi : B \to \mathbb { C }$ be a Banach algebra homomorphism. What can you say about its norm? What if some element of norm less than 1 goes to the number 1?

## 6 Lp Spaces

Question 6.1. When is Lp contained in Lq? Prove it. For what measure is this containment reversed? Prove it.

Question 6.2. State H¨older’s inequality. When does equality hold?

Question 6.3. Tell me a function that is in $L ^ { 2 }$ but not in $L ^ { 1 }$

Question 6.4. Is there a function in $L ^ { 1 } ( [ 0 , 1 ] )$ which is not in $L ^ { \boldsymbol { p } } ( [ 0 , 1 ] ) \boldsymbol { \sharp }$

Question 6.5. When is the function $1 / x ^ { a }$ in $L ^ { p }$ over $\begin{array} { r } { [ 0 , 1 ] \stackrel { \_ } { \cdot } { \cal O } n \left[ 0 , \infty \right) \stackrel { \_ } { \cdot } } \end{array}$ What about the function $1 / ( x ^ { a } ( \log x ) ^ { b } ) \ ?$

Question 6.6. Define \`p. What inclusions are there between these spaces for different values $o f p \ell$ What about $L ^ { p } \boldsymbol { \ ? }$ Inclusion?

Question 6.7. Prove the completeness of Lp.

Question 6.8. Prove that continuous functions are dense in $L ^ { 1 }$ over a compact space. What about a noncompact space? What about for Lp instead of $L ^ { 1 } \mathcal { ? }$

Question 6.9. Why are continuous functions of compact support dense in $L ^ { p } \boldsymbol { \ ? }$

Question 6.10. Is $L ^ { 1 } [ a , b ]$ compact? Find a precompact subspace of $L ^ { 1 }$

Question 6.11. Characterise the compact subsets of an Lp space.

Question 6.12. Give an orthonormal basis for $L ^ { 2 } ( \mathbb { R } )$

Question 6.13. Why isn’t Lp a Hilbert space for p different from 2?

Question 6.14. Prove that the dual of Lp is Lq, where $1 < p < \infty$ and $1 / p + 1 / q = 1$ Explain what can go wrong and give examples for $p = 1$ . Show that the dual to $L ^ { \infty }$ contains elements that are not given by integrating against $L ^ { 1 }$ elements.

Question 6.15. If a function in $L ^ { 1 }$ has one derivative in $L ^ { 1 }$ , what can you say? So, what can you say if a function has all derivatives in $L ^ { 1 } ?$

Question 6.16. If you have a function on the plane whose gradient is in $L ^ { 2 }$ , what can you say about its decay?

Question 6.17. Do you know what a weak derivative is? Let u be a compactly supported function on $\mathbb { R } ^ { 2 }$ . Can you bound an $L ^ { p }$ norm of u in terms of the integral over $\mathbb { R } ^ { 2 }$ of the length of the gradient of u?

Question 6.18. Suppose $f : \mathbb { R } / \mathbb { Z } \to \mathbb { R }$ is differentiable, $f ( 0 ) = 0$ and the $L ^ { 2 }$ norm of f 0 is finite. Bound $\| f \| _ { \infty }$ Suppose now f is on $( \mathbb { R } / \mathbb { Z } ) ^ { 2 } , f ( 0 , 0 ) = 0$ , and both its derivatives have finite $L ^ { 2 }$ norms. Can you still bound $\| f \| _ { \infty } \ell$ What if you have similar bounds on second derivatives?

## 7 Convolution

Question 7.1. Suppose you have a function f, and you define a function g as $g ( x ) = f ( t - x )$ What can you say about the integral of f times $g \smash { \ell }$ When will it be finite? Is it continuous with respect to t?

Question 7.2. Let $\begin{array} { r } { h ( x ) = \int _ { \mathbb R } f ( x - y ) g ( y ) d y } \end{array}$ . What can you say about it if both f and g are in $L ^ { 2 } ?$

Question 7.3. Take f in Lp, g in Lq (not necessarily conjugate exponents). What can you say about their convolution? What if they are conjugate exponents? Prove that, in that case, f ∗ g is continuous and tends to 0 at infinity.

Question 7.4. How/why does convolution tend to produce smoother functions?

Question 7.5. What can you say about convolution kernels and their properties? Give an example of a summability kernel. Discuss relations with the Dirac delta.

Question 7.6. What are approximations to the identity? Can you have approximations to the identity that do not have compact support?

Question 7.7. Why are $C _ { 0 } ^ { \infty }$ functions dense in Lp? How do you approximate the characteristic (indicator) function of [0, 1] by $C _ { 0 } ^ { \infty }$ functions?

## 8 Different Kinds of Convergence

Question 8.1. Define different notions of convergence for functions on [0, 1]. Which modes of convergence imply which others? When does convergence in Lp norm imply convergence in Lq norm?

Question 8.2. Suppose you have a sequence of continuous functions on [0, 1], pointwise convergent to some function. Does it have to converge uniformly? What if the functions decrease to zero? Prove it.

Question 8.3. A sequence of continuous functions converges pointwise. What is a condition you can impose to make the limit continuous?

Question 8.4. Discuss uniform convergence and some useful criteria related to it.

Question 8.5. Given a sequence of continuous functions from [0, 1] to R that tends to 0 pointwise, do their integrals tend to 0? Give a counterexample.

Question 8.6. If a sequence of functions converges uniformly to 0 on a finite measure space, do its integrals also do so? On an infinite measure space?

Question 8.7. Let $f _ { n }$ be a convergent sequence of functions on a compact interval whose derivatives are bounded. Is the convergence uniform? Prove it or give a counterexample.

Question 8.8. What relations are there between L1, L∞, and pointwise convergence? Give counterexamples in the opposite directions.

Question 8.9. In the setting of functions from, say, [0, 1] to R, what’s uniform continuity? Prove that the uniform limit of a sequence of continuous functions is continuous. If a sequence of differentiable functions converges uniformly to a differentiable function, does the sequence of derivatives converge to the derivative of the limit? Give a proof or counterexample. What about in the complex case?

Question 8.10. What conditions do you know that make the derivatives of a pointwiseconvergent sequence of functions also converge pointwise? Does convexity do it?

Question 8.11. Give an example of functions on [0, 1] that converge in L1 but not almost everywhere. Can you give an example where they converge nowhere?

Question 8.12. Give a sequence of functions that converge in all the Lp spaces but not pointwise.

Question 8.13. Do you know a sequence of functions on [0, 1] whose integrals converge to zero yet converges nowhere?

Question 8.14. Give an example of a sequence of L1 functions on [0, 1] converging pointwise to a limit that is not integrable.

Question 8.15. Consider the powers of the continuous function f defined on [0, 1]. State and prove a theorem about uniform convergence of the powers of f to 0 on [0, 1].

Question 8.16. If F is a positive L1 function on R, define $F _ { n } ( x ) = F ( x + n )$ . Show that there is a subsequence converging to zero almost everywhere.

Question 8.17. What theorems do you know about selecting a convergent subsequence? Prove one of them. What about for complex numbers?

Question 8.18. What is a condition you can impose on a sequence (of functions) to ensure the existence of a uniformly convergent subsequence?

Question 8.19. State/prove the Arzel\`a–Ascoli theorem.

## 9 Differentiation

Question 9.1. Is it true that for every sequence of real numbers $a _ { n }$ there exists a function whose $n ^ { t h }$ derivative at zero is equal to $a _ { n }$ for all n?

Question 9.2. Write down a function which is everywhere differentiable, but whose derivative is not continuous.

Question 9.3. If you have a function which is almost everywhere differentiable with derivative 0, must it be constant? Construct a counterexample.

Question 9.4. What differentiability properties does a monotone function have?

Question 9.5. Give an example of a differentiable function on [0, 1] with derivative NOT in $L ^ { 1 }$

Question 9.6. What is the Taylor expansion formula with remainder? What does it mean that a function is analytic in terms of the remainder? If the zeros of an analytic function have an accumulation point, what is happening? Prove it.

Question 9.7. Can you give an example of a function that decays faster than any polynomial, but whose derivatives do not?

Question 9.8. Give an example of an everywhere-continuous, nowhere-differentiable function on the unit interval.

Question 9.9. Give an example of a real-valued real analytic function on R whose power series at zero does not represent it everywhere.

Question 9.10. What functions are differentiable almost everywhere?

## 10 Absolute Continuity and Bounded Variation

Question 10.1. Prove that functions of bounded variation are continuous almost everywhere.

Question 10.2. Prove that a function of bounded variation is the sum of two monotone functions.

Question 10.3. Define the total variation of a real-valued function on a closed interval. What can be said about the differentiability of a function of bounded variation?

Question 10.4. Is the derivative of a function of bounded variation in $L ^ { 1 } \mathcal { ? }$

Question 10.5. If a function is continuous and of bounded variation, is it absolutely continuous? Give a counterexample.

Question 10.6. Say that F defined on $[ a , b ]$ satisfies $\begin{array} { r } { F ( x ) - F ( a ) = \int _ { a } ^ { x } f ( t ) } \end{array}$ dt for an $L ^ { 1 }$ function f . Is F of bounded variation? What is its total variation? What is the relation between functions of bounded variation and monotone functions?

Question 10.7. If a function is of bounded variation on [a, b] is it necessarily equal to the integral of its derivative? (assuming the latter exists almost everywhere!) What is special about functions that DO equal the integral of their derivative?

Question 10.8. What is the relation between absolutely continuous functions and absolutely continuous measures (with respect to the Lebesgue measure)?

Question 10.9. What is a necessary and sufficient condition for a function to be the indefinite integral of its derivative?

Question 10.10. Suppose you have a sequence of functions $f _ { n }$ of bounded variation on a compact interval $[ a , b ]$ , normalised so that $f _ { n } ( a ) \ = \ 0$ for all n, and such that their total variations are uniformly bounded, i.e., there exists a constant $C > 0$ independent of n, such that $T f _ { n } ( b ) < C$ for all n. What can you conclude?

Question 10.11. What is the Lipschitz condition? Does the Lipschitz condition imply absolute continuity? What $i f \left| f ( x ) - f ( y ) \right| < C | x - y | ^ { \alpha } ~ f o r ~ 0 < \alpha < 1 \mathcal {? }$

Question 10.12. How much regularity do you need to do integration by parts? Does it work for Lipschitz functions? Can you do it for functions of bounded variation?

## 11 Lebesgue Differentiation Theorem

Question 11.1. Define the Hardy–Littlewood maximal function. What does it do to functions in Lp? Give a counterexample showing it does not map L1 into L1.

Question 11.2. State the Lebesgue differentiation theorem. What are the main tools used in the proof ? Define the maximal function. What are the main results concerning it?

Question 11.3. State/prove the Vitali covering lemma.

Question 11.4. What would the Lebesgue differentiation theorem mean when applied to a characteristic (indicator) function?

Question 11.5. What is a density point? What can you say about them? If I have a set of positive measure on the real line, show that it has a point of density. State the fundamental theorem of calculus and explain the relation to points of density.

Question 11.6. Is there a probability measure µ on [0, 1] such that

$$
\operatorname* { l i m } _ { \varepsilon \to 0 } { \frac { \log \mu ( [ x - \varepsilon , x + \varepsilon ] ) } { \log \varepsilon } } > 1 . 5
$$

for almost every x?

## 12 Category, Completeness, Continuity, and Convexity

Question 12.1. What are Baire categories?

Question 12.2. State/prove Baire’s theorem.

Question 12.3. Discuss various notions of a set being “small”.

Question 12.4. Give an example of a meagre set of full measure. Present an example of a set of the first category of full measure (note that “meagre” and “first category” mean the same thing).

Question 12.5. Give an example of a residual set of measure zero.

Question 12.6. Can you find a sequence of continuous functions converging pointwise to the characteristic (indicator) function of the rationals? What sets of discontinuity are possible for pointwise limits of continuous functions?

Question 12.7. Suppose a sequence of continuous functions has integrals converging to 0. Maybe also assume that they converge pointwise. Does the limit have to be continuous somewhere?

Question 12.8. Is there a function on [0, 1] which is discontinuous at every rational point (and nowhere else)? Prove it. How about at every irrational point? Prove that. Do you know a function continuous on only the irrationals?

Question 12.9. Consider the set of irrational numbers in the unit interval. What can you say about closed subsets thereof ?

Question 12.10. Can you construct a Peano curve?

Question 12.11. State the inverse function theorem.

Question 12.12. What can you say about convex functions? Specifically, can a convex function have countably many points of non-differentiability? Could these points have an accumulation point? Could there be uncountably many points of non-differentiability?

Question 12.13. Define a convex function. What do you know about them? How smooth must a convex function be? Does it have a second derivative? Is there a convex function with second derivative almost everywhere 0 but which is not linear in any interval?

Question 12.14. Having a convex function, its second derivative is nonnegative. How could you generalise this for functions not having second derivative? For instance, for f (x) = |x|.

## 13 Probability

Question 13.1. State/prove the central limit theorem.

Question 13.2. Give the asymptotics for the nth moment of the standard normal distribution. What is the name of the formula? Do you know it for complex values of the parameter? Talk about a multi-dimensional version of the method you used to calculate them.

Question 13.3. What is a conditional expectation? Why does it exist?

Question 13.4. What is the relation between convolution and the distribution function of the sum of two random variables?

## 14 Differential Equations

Question 14.1. Consider the problem: (i) $y ^ { \prime } = f ( y ) \ ( i i ) \ y ( x _ { 0 } ) = y _ { 0 }$ . What are sufficient conditions for the existence of a solution?

Question 14.2. What does it mean for a function to satisfy a Lipschitz condition? What does this imply about the distributional derivative? If f : R → R is Lipschitz, what can you say about the ODE $d x / d t = f ( x ) \ ?$ Do you know the idea of the proof ? Does the proof work if R is replaced by Rn? By a Banach space?

Question 14.3. Give an expression for the first Dirichlet eigenvalue of a domain in Rn.

Question 14.4. What is the difference between holomorphic and C∞? Which property is useful for proving global PDE theorems?

Question 14.5. Can you use ODEs to prove the uniqueness of the Jordan canonical form over real/complex numbers?

## 15 Harmonic Functions

Question 15.1. Take a $C ^ { 2 }$ harmonic function on a bounded domain with smooth boundary which is continuous on the boundary, 0 on a boundary segment, and whose normal derivative on that segment is 0. What can you say?

Question 15.2. Give a pointwise upper bound for a harmonic function in a domain of $\mathbb { R } ^ { n }$ if its gradient squared integrates to 1, depending only on the distance from the boundary.

Question 15.3. Find all positive-valued harmonic functions on the complex plane.

Question 15.4. What are the bounded harmonic functions outside a ball?

## 16 Asymptotics

Question 16.1. Given a smooth $f : [ 0 , 1 ] \to \mathbb { R }$ , describe how $\begin{array} { r } { \int _ { 0 } ^ { 1 } \exp ( t f ( x ) ) } \end{array}$ dx behaves as $t \to \infty$

Question 16.2. How would you estimate the behaviour as $n \to \infty$ of this integral?

$$
\int _ { \mathbb { R } } x ^ { 2 n } e ^ { - n x ^ { 4 } } d x
$$

Question 16.3. Suppose f is a smooth doubly periodic function. How does the average value on a circle with fixed center grow as the radius tends to infinity?

## 17 Sequences and Series

Question 17.1. When does the sum of $1 / n ^ { p }$ (for fixed real p) converge? What does this imply if we replace p by a complex number?

Question 17.2. Consider the series

$$
1 - 1 / 2 + 1 / 3 - 1 / 4 + . . .
$$

What does this converge to? Can you show why this converges? Can you rearrange the series to converge to something else? What’s a general statement about the convergence of alternating series?

Question 17.3. Evaluate the limit as n goes to infinity of

$$
{ \frac { 1 } { n } } + { \frac { 1 } { n + 1 } } + \ldots + { \frac { 1 } { 2 n } } .
$$

Question 17.4. ${ \cal I f a } _ { n }$ is an enumeration of the rational numbers in [0, 1], does the series

$$
\sum _ { n = 1 } ^ { \infty } { \frac { 1 } { 2 ^ { n } } } { \frac { 1 } { \sqrt { x - a _ { n } } } }
$$

converge anywhere on $[ 0 , 1 ] \ell$

Question 17.5. $H f a _ { n }$ is an enumeration of the rationals in [0, 1] and we write $a _ { n } = p _ { n } / q _ { n }$ in lowest terms, what can you say about the sum below?

$$
f ( x , s ) = \sum _ { n = 1 } ^ { \infty } { \frac { 1 } { ( p _ { n } x + q _ { n } ) ^ { s } } }
$$

## 18 Diophantine Problems

Question 18.1. What kind of set is the set of all $x \in \mathbb { R }$ such that for infinitely many positive integers q there exists a rational number p/q such that $| x - p / q | < \exp ( - q ) \ ?$

Question 18.2. Given an irrational number a, and a continuous function f on the circle, show that as $N  \infty$ the average of f on the point $e ^ { 2 \pi i a } , e ^ { 2 \pi i 2 a } , e ^ { 2 \pi i 3 a } , . . . , e ^ { 2 \pi i N a }$ tends to the average of f on the circle. Hint: this is easily proven for $f ( z ) = z ^ { k }$

Question 18.3. Given a function $h \in L ^ { 2 } ( \mathbb { T } )$ and an irrational t, when and how can you find an $f \in L ^ { 2 } ( \mathbb { T } )$ such that $f ( x + t ) - f ( x ) = h ( x )$ almost everywhere?

Question 18.4. Suppose you have an irrational number t. Why are the fractional parts of nt equidistributed on [0, 1] as n ranges over the whole numbers?