# revision 15878
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-2dplot
# catalog-date 2006-12-31 09:43:01 +0000
# catalog-license lppl
# catalog-version 1.5
Name:		texlive-pst-2dplot
Version:	1.5
Release:	1
Summary:	A PSTricks package for drawing 2D curves
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-2dplot
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-2dplot.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-2dplot.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Pst-2dplot is a pstricks package that offers an easy-to-use and
intuitive tool for plotting 2-d curves. It defines an
environment with commands similar to MATLAB for plotting.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pst-2dplot/pst-2dplot.sty
%doc %{_texmfdistdir}/doc/generic/pst-2dplot/README
%doc %{_texmfdistdir}/doc/generic/pst-2dplot/data1.dat
%doc %{_texmfdistdir}/doc/generic/pst-2dplot/data2.dat
%doc %{_texmfdistdir}/doc/generic/pst-2dplot/data3.dat
%doc %{_texmfdistdir}/doc/generic/pst-2dplot/pst-2dplot-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-2dplot/pst-2dplot-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
