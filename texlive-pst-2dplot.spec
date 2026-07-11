%global tl_name pst-2dplot
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.5
Release:	%{tl_revision}.1
Summary:	A PSTricks package for drawing 2D curves
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-2dplot
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-2dplot.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-2dplot.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Pst-2dplot is a pstricks package that offers an easy-to-use and
intuitive tool for plotting 2-d curves. It defines an environment with
commands similar to MATLAB for plotting.

