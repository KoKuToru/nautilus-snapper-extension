# Maintainer: Luca Béla Palkovics <luca.bela.palkovics@gmail.com>

pkgrel=1
pkgver=20150120
pkgname=('nautilus-snapper-extension')
pkgdesc="Extension for nautilus, adds ability to open old versions of files"
url="https://github.com/KoKuToru/gTox.git"
license='GPL2'
arch=('i686' 'x86_64')
depends=('nautilus-python' 'xdg-utils')
makedepends=()
source=(.AURINFO "${pkgname%-git}::git+https://github.com/KoKuToru/nautilus-snapper-extension.git")
sha256sums=('SKIP' 'SKIP')
provides=('nautilus-snapper-extension')
conflicts=('nautilus-snapper-extension')

pkgver()
{
     cd ${pkgname%-git}
     git log -1 --format="%cd" --date=short | sed "s|-||g"
}

build()
{
    #do nothing
}

package()
{
	cp ${pkgname%-git}/*.py ${pkgdir}/usr/share/nautilus-python/extensions/
}
