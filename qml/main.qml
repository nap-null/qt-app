import QtQuick 2.0
import QtQuick.Controls 2.12
import QtQuick.Layouts 1.15

ApplicationWindow
{
    visible: true
    title: "Example"
    width: 400
    height: 400

    Label {
        anchors.centerIn: parent
        text: qsTr("Hello World!")
        font.pixelSize: 14
    }
}