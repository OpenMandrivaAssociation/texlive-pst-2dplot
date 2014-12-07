# revision 15878
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-2dplot
# catalog-date 2006-12-31 09:43:01 +0000
# catalog-license lppl
# catalog-version 1.5
Name:		texlive-pst-2dplot
Version:	1.5
Release:	9
Summary:	A PSTricks package for drawing 2D curves
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-2dplot
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-2dplot.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-2dplot.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Pst-2dplot is a pstricks package that offers an easy-to-use and
intuitive tool for plotting 2-d curves. It defines an
environment with commands similar to MATLAB for plotting.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.5-2
+ Revision: 755153
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.5-1
+ Revision: 719326
- texlive-pst-2dplot
- texlive-pst-2dplot
- texlive-pst-2dplot
- texlive-pst-2dplot

