Name:		texlive-spelling
Version:	30715
Release:	1
Summary:	Support for spell-checking of LuaTeX documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/luatex/generic/spelling
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spelling.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spelling.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package aids spell-checking of TeX documents compiled with
the LuaTeX engine. It can give visual feedback in PDF output
similar to WYSIWYG word processors. The package relies on an
external spell-checker application to check spelling of a text
file and to output a list of bad spellings. The package should
work with most spell-checkers, even dumb, TeX-unaware ones.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/scripts/spelling/spelling-main.lua
%{_texmfdistdir}/scripts/spelling/spelling-recurse.lua
%{_texmfdistdir}/scripts/spelling/spelling-stage-1.lua
%{_texmfdistdir}/scripts/spelling/spelling-stage-2.lua
%{_texmfdistdir}/scripts/spelling/spelling-stage-3.lua
%{_texmfdistdir}/scripts/spelling/spelling-stage-4.lua
%{_texmfdistdir}/tex/luatex/spelling/spelling.sty
%doc %{_texmfdistdir}/doc/luatex/spelling/CHANGES
%doc %{_texmfdistdir}/doc/luatex/spelling/LICENSE
%doc %{_texmfdistdir}/doc/luatex/spelling/README
%doc %{_texmfdistdir}/doc/luatex/spelling/spelling-doc-lst-lua.tex
%doc %{_texmfdistdir}/doc/luatex/spelling/spelling-doc.bad
%doc %{_texmfdistdir}/doc/luatex/spelling/spelling-doc.pdf
%doc %{_texmfdistdir}/doc/luatex/spelling/spelling-doc.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar scripts tex doc %{buildroot}%{_texmfdistdir}
