#include <QApplication>
#include <QQmlApplicationEngine>
#include <QtPlugin>
#include <QtGlobal>


#ifdef BUILD_STATIC
    Q_IMPORT_PLUGIN(QtQmlPlugin)
    Q_IMPORT_PLUGIN(QtQmlModelsPlugin)
    Q_IMPORT_PLUGIN(QtQmlWorkerScriptPlugin)
    Q_IMPORT_PLUGIN(QtQuick2Plugin)
    Q_IMPORT_PLUGIN(QtQuickControls2Plugin)
    Q_IMPORT_PLUGIN(QtQuickLayoutsPlugin)
    Q_IMPORT_PLUGIN(QtQuickTemplates2Plugin)
    Q_IMPORT_PLUGIN(QtQuick2WindowPlugin)

    #ifdef IOS
        Q_IMPORT_PLUGIN(QIOSIntegrationPlugin)
    #endif
#endif


int main(int argc, char* argv[]) {
    QApplication app(argc, argv);
    QQmlApplicationEngine engine;

    engine.load(QUrl(QStringLiteral("qrc:/qml/main.qml")));

    return app.exec();
}
