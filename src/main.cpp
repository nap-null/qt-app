#include <QGuiApplication>
#include <QQmlApplicationEngine>


int main(int argc, char* argv[]) {
    QGuiApplication app(argc, argv);
    QQmlApplicationEngine engine;

    engine.load(QUrl(QStringLiteral("qrc:/qt_app/qml/main.qml")));

    return app.exec();
}
