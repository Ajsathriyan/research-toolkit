

from modules.export import export_csv
from PySide6.QtWidgets import QMessageBox
from PySide6.QtGui import QAction
from modules.export import export_dataframe
from PySide6.QtGui import QPixmap
from PySide6.QtGui import QIcon
from modules.graphs import (
    histogram,
    box_plot,
    scatter_plot,
    regression_plot,
    qq_plot,
    bland_altman_plot,
)
from modules.statistics import linear_regression
from modules.statistics import auto_correlation
from modules.analysis import auto_independent_test
from modules.analysis import auto_paired_test
from modules.statistics import descriptive_statistics
from modules.excel import load_excel

from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QLabel,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QHBoxLayout,
    QGroupBox,
    QFileDialog,
    QComboBox,
)

from PySide6.QtCore import Qt


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.df = None
        self.current_result = None
        self.setWindowIcon(QIcon("icons/logo.png"))
        self.setWindowTitle("AJ Research Toolkit")
        self.resize(1200, 750)
        # ================= MENU BAR =================
        
        menubar = self.menuBar()
        
        file_menu = menubar.addMenu("File")
        analysis_menu = menubar.addMenu("Analysis")
        graph_menu = menubar.addMenu("Graphs")
        export_menu = menubar.addMenu("Export")
        help_menu = menubar.addMenu("Help")
        
        open_action = QAction("Open Excel", self)
        save_action = QAction("Export Results", self)
        exit_action = QAction("Exit", self)
        # Analysis Menu

        desc_action = QAction("Descriptive Statistics", self)
        paired_action = QAction("Paired Test", self)
        ind_action = QAction("Independent Test", self)
        corr_action = QAction("Correlation", self)
        reg_action = QAction("Linear Regression", self)
        scatter_action = QAction("Scatter Plot", self)
        hist_action = QAction("Histogram", self)
        box_action = QAction("Box Plot", self)
        qq_action = QAction("QQ Plot", self)
        ba_action = QAction("Bland-Altman Plot", self)
        about_action = QAction("About AJ Research Toolkit", self)

        help_menu.addAction(about_action)
        
        about_action.triggered.connect(self.show_about)
        # Export Menu

        export_excel_action = QAction("Export to Excel", self)
        export_csv_action = QAction("Export to CSV", self)
       

        export_menu.addAction(export_excel_action)
        export_menu.addAction(export_csv_action)
        export_menu.addSeparator()
       
                
        
        analysis_menu.addAction(desc_action)
        analysis_menu.addAction(paired_action)
        analysis_menu.addAction(ind_action)
        analysis_menu.addAction(corr_action)
        analysis_menu.addAction(reg_action)
        
        graph_menu.addAction(scatter_action)
        graph_menu.addAction(hist_action)
        graph_menu.addAction(box_action)
        graph_menu.addAction(qq_action)
        graph_menu.addAction(ba_action)
        
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        file_menu.addSeparator()
        file_menu.addAction(exit_action)

        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QHBoxLayout()
        
        # ---------------- Status Bar ----------------

        self.statusBar().showMessage("Ready")

        # ---------------- Left Panel ----------------
        left_panel = QVBoxLayout()
        # Logo
        logo = QLabel()
        
        from resource_path import resource_path

        pixmap = QPixmap(resource_path("icons/logo.png"))
        pixmap = pixmap.scaled(
            120,
            120,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        
        logo.setPixmap(pixmap)
        logo.setAlignment(Qt.AlignCenter)
        
        left_panel.addWidget(logo)
        
        # Title
        title = QLabel("AJ Research Toolkit")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            font-size:24px;
            font-weight:bold;
            color:#1f4e79;
        """)
        
        left_panel.addWidget(title)

        # ---------------- File Group ----------------

        file_group = QGroupBox("Excel File")
        file_layout = QVBoxLayout()

        self.btn_open = QPushButton("Open Excel File")

        file_layout.addWidget(self.btn_open)
        file_group.setLayout(file_layout)

        left_panel.addWidget(file_group)

        # ---------------- Analysis Group ----------------

        analysis_group = QGroupBox("Analysis")
        analysis_layout = QVBoxLayout()

        self.btn_desc = QPushButton("Descriptive Statistics")

        self.combo1 = QComboBox()
        self.combo2 = QComboBox()

        analysis_layout.addWidget(QLabel("Variable 1"))
        analysis_layout.addWidget(self.combo1)

        analysis_layout.addWidget(QLabel("Variable 2"))
        analysis_layout.addWidget(self.combo2)

        self.btn_paired = QPushButton("Paired Test")
        self.btn_independent = QPushButton("Independent Test")
        self.btn_corr = QPushButton("Correlation")
        self.btn_regression = QPushButton("Linear Regression")
        self.btn_scatter = QPushButton("Scatter Plot")
        self.btn_histogram = QPushButton("Histogram")
        self.btn_box = QPushButton("Box Plot")
        self.btn_regression_plot = QPushButton("Regression Plot")
        self.btn_qq = QPushButton("QQ Plot")
        self.btn_bland = QPushButton("Bland-Altman Plot")
        self.btn_export = QPushButton("Export Results")
        
        
        
        # Disable analysis buttons until an Excel file is loaded
        self.btn_desc.setEnabled(False)
        self.btn_paired.setEnabled(False)
        self.btn_independent.setEnabled(False)
        self.btn_corr.setEnabled(False)
        self.btn_regression.setEnabled(False)
        self.btn_scatter.setEnabled(False)
        self.btn_histogram.setEnabled(False)
        self.btn_box.setEnabled(False)
        self.btn_regression_plot.setEnabled(False)
        self.btn_qq.setEnabled(False)
        self.btn_bland.setEnabled(False)
        self.btn_export.setEnabled(False)
                
        # Disable column selectors
        self.combo1.setEnabled(False)
        self.combo2.setEnabled(False)

        analysis_layout.addWidget(self.btn_desc)
        analysis_layout.addWidget(self.btn_paired)
        analysis_layout.addWidget(self.btn_independent)
        analysis_layout.addWidget(self.btn_corr)
        analysis_layout.addWidget(self.btn_regression)
        analysis_layout.addWidget(self.btn_scatter)
        analysis_layout.addWidget(self.btn_histogram)
        analysis_layout.addWidget(self.btn_box)
        analysis_layout.addWidget(self.btn_regression_plot)
        analysis_layout.addWidget(self.btn_qq)
        analysis_layout.addWidget(self.btn_bland)
        analysis_layout.addWidget(self.btn_export)

        analysis_group.setLayout(analysis_layout)

        left_panel.addWidget(analysis_group)
        left_panel.addStretch()

        # ---------------- Right Panel ----------------
        self.output = QTextEdit()
        self.output.setReadOnly(True)
        
        
        main_layout.addLayout(left_panel, 1)
        main_layout.addWidget(self.output, 3)
        central.setLayout(main_layout)
        
         # Welcome Widget
        self.welcome = QWidget()
        
        welcome_layout = QVBoxLayout()

        welcome_layout.setAlignment(Qt.AlignCenter)
        welcome_layout.setSpacing(15)
        
        welcome_layout.addStretch()
        
        # Logo
        logo = QLabel()
        
        pixmap = QPixmap("icons/logo.png")
        pixmap = pixmap.scaled(
            220,
            220,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        
        logo.setPixmap(pixmap)
        logo.setAlignment(Qt.AlignCenter)
        
        welcome_layout.addWidget(logo)
        
        # Title
        title = QLabel("AJ Research Toolkit")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
        font-size:28px;
        font-weight:bold;
        color:#1f4e79;
        """)
        
        welcome_layout.addWidget(title)
        
        # Subtitle
        subtitle = QLabel("Statistical Analysis Software")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setStyleSheet("""
        font-size:18px;
        color:#555555;
        """)
        
        welcome_layout.addWidget(subtitle)
        
        # Description
        description = QLabel(
            "Biomedical Research • Medical Physics • Clinical Research"
        )
        
        description.setAlignment(Qt.AlignCenter)
        
        description.setStyleSheet("""
        font-size:14px;
        color:gray;
        """)
        
        welcome_layout.addWidget(description)
        
        welcome_layout.addSpacing(20)
        
        developer = QLabel("""
        Developed by
        
        Ajithkumar M
        
        Department of Medical Physics
        
        National Cancer Institute (NCI)
        
        AIIMS Jhajjar, Haryana
        """)
        
        developer.setAlignment(Qt.AlignCenter)
        
        developer.setStyleSheet("""
        font-size:13px;
        color:#444444;
        """)
        
        welcome_layout.addWidget(developer)
        
        welcome_layout.addStretch()
        
        self.welcome.setLayout(welcome_layout)
        
        # Stacked Widget
        from PySide6.QtWidgets import QStackedWidget
        
        self.stack = QStackedWidget()
        
        self.stack.addWidget(self.welcome)
        self.stack.addWidget(self.output)
        
        main_layout.addLayout(left_panel,1)
        main_layout.addWidget(self.stack,3)

        # ---------------- Connect Buttons ----------------

        self.btn_open.clicked.connect(self.open_excel)
        self.btn_desc.clicked.connect(self.run_descriptive)
        self.btn_paired.clicked.connect(self.run_paired_test)
        self.btn_independent.clicked.connect(self.run_independent_test)
        self.btn_corr.clicked.connect(self.run_correlation)
        self.btn_regression.clicked.connect(self.run_regression)
        self.btn_scatter.clicked.connect(self.run_scatter)
        self.btn_histogram.clicked.connect(self.run_histogram)
        self.btn_box.clicked.connect(self.run_boxplot)
        self.btn_regression_plot.clicked.connect(self.run_regression_plot)
        self.btn_qq.clicked.connect(self.run_qq_plot)
        self.btn_bland.clicked.connect(self.run_bland_altman)
        self.btn_export.clicked.connect(self.export_results)
        open_action.triggered.connect(self.open_excel)
        save_action.triggered.connect(self.export_results)
        exit_action.triggered.connect(self.close)
        desc_action.triggered.connect(self.run_descriptive)
        paired_action.triggered.connect(self.run_paired_test)
        ind_action.triggered.connect(self.run_independent_test)
        corr_action.triggered.connect(self.run_correlation)
        reg_action.triggered.connect(self.run_regression)
        scatter_action.triggered.connect(self.run_scatter)
        export_excel_action.triggered.connect(self.export_results)
        export_csv_action.triggered.connect(self.export_csv_file)
        save_graph_action = QAction("Save Graph", self)

        export_menu.addAction(save_graph_action)
        
        save_graph_action.triggered.connect(self.save_graph)
        hist_action.triggered.connect(self.run_histogram)

        box_action.triggered.connect(self.run_boxplot)
        
        qq_action.triggered.connect(self.run_qq_plot)
        
        ba_action.triggered.connect(self.run_bland_altman)


    def open_excel(self):

        filename, _ = QFileDialog.getOpenFileName(
            self,
            "Open Excel File",
            "",
            "Excel Files (*.xlsx *.xls)"
        )

        if not filename:
            return

        self.df = load_excel(filename)

        if self.df is None:
            self.output.setText("Failed to load Excel file.")
            self.statusBar().showMessage(f"Loaded: {filename}")
            return

        # Populate Combo Boxes

        self.combo1.clear()
        self.combo2.clear()

        numeric_columns = self.df.select_dtypes(include="number").columns

        self.combo1.addItems(numeric_columns)
        self.combo2.addItems(numeric_columns)
        
        # Enable analysis controls
        self.btn_desc.setEnabled(True)
        self.btn_paired.setEnabled(True)
        self.btn_independent.setEnabled(True)
        self.btn_corr.setEnabled(True)
        self.btn_regression.setEnabled(True)
        self.btn_scatter.setEnabled(True)
        self.btn_histogram.setEnabled(True)
        self.btn_box.setEnabled(True)
        self.btn_regression_plot.setEnabled(True)
        self.btn_qq.setEnabled(True)
        self.btn_bland.setEnabled(True)
        self.btn_export.setEnabled(True)
        
        
        self.combo1.setEnabled(True)
        self.combo2.setEnabled(True)

        # Display File Information

        text = f"Loaded:\n{filename}\n\n"
        text += f"Rows : {len(self.df)}\n"
        text += f"Columns : {len(self.df.columns)}\n\n"

        text += "Available Columns\n"
        text += "-" * 25 + "\n"

        for col in self.df.columns:
            text += f"• {col}\n"

        self.output.setText(text)
        self.stack.setCurrentWidget(self.output)

    def run_descriptive(self):

        if self.df is None:
            self.output.setText("Please open an Excel file first.")
            return

        stats = descriptive_statistics(self.df)

        self.current_result = stats
        self.output.setText(stats.to_string(index=False))
        self.statusBar().showMessage("Descriptive Statistics completed")

    def run_paired_test(self):

        if self.df is None:
            self.output.setText("Please open an Excel file first.")
            return

        col1 = self.combo1.currentText()
        col2 = self.combo2.currentText()

        if col1 == col2:
            self.output.setText("Please select two different variables.")
            return

        result = auto_paired_test(self.df, col1, col2)

        text = ""

        for key, value in result.items():
            text += f"{key}: {value}\n"

        self.current_result = result
        self.output.setText(text)
        self.statusBar().showMessage("Paired Test completed")
        
        
    def run_independent_test(self):

        if self.df is None:
            self.output.setText("Please open an Excel file first.")
            return
    
        col1 = self.combo1.currentText()
        col2 = self.combo2.currentText()
    
        if col1 == col2:
            self.output.setText("Please select two different variables.")
            
            return
    
        result = auto_independent_test(self.df, col1, col2)
    
        text = ""
    
        for key, value in result.items():
            text += f"{key}: {value}\n"
    
        self.current_result = result
        self.output.setText(text)
        self.statusBar().showMessage("Independent Test completed")
        
        
    def run_correlation(self):

        if self.df is None:
            self.output.setText("Please open an Excel file first.")
            return
    
        col1 = self.combo1.currentText()
        col2 = self.combo2.currentText()
    
        if col1 == col2:
            self.output.setText("Please select two different variables.")
            
            return
    
        result = auto_correlation(self.df, col1, col2)
    
        text = ""
    
        for key, value in result.items():
            text += f"{key}: {value}\n"
    
        self.current_result = result
        self.output.setText(text)
        self.statusBar().showMessage("Correlation completed")
        
    def run_regression(self):

        if self.df is None:
            self.output.setText("Please open an Excel file first.")
            return
    
        x = self.combo1.currentText()
        y = self.combo2.currentText()
    
        if x == y:
            self.output.setText("Please select two different variables.")
            return
    
        result = linear_regression(self.df, x, y)
    
        text = ""
        text += "LINEAR REGRESSION\n"
        text += "=" * 35 + "\n\n"
    
        for key, value in result.items():
            text += f"{key}: {value}\n"
    
        self.current_result = result
        self.output.setText(text)
        self.statusBar().showMessage("Linear Regression completed")
        
    def run_scatter(self):

        if self.df is None:
            self.output.setText("Please open an Excel file first.")
            return
    
        x = self.combo1.currentText()
        y = self.combo2.currentText()
    
        if x == y:
            self.output.setText("Please select two different variables.")
            return
    
        from gui.graph_settings import GraphSettings

        dialog = GraphSettings()

        if dialog.exec():

           color = dialog.color.currentText()
           marker = dialog.marker.currentText()
           size = dialog.size.value()

        scatter_plot(
           self.df,
           x,
           y,
           color=color,
           marker=marker,
           size=size
        )
    
        self.output.setText(
            f"Scatter plot created successfully.\n\n"
            f"X-axis : {x}\n"
            f"Y-axis : {y}"
        )
        self.statusBar().showMessage("Scatter Plot created")
        
    def run_histogram(self):

        if self.df is None:
            return
    
        column = self.combo1.currentText()
    
        histogram(self.df, column)
    
        self.output.setText(
            f"Histogram created successfully.\n\n"
            f"Variable : {column}"
        )
        
    def run_boxplot(self):

        if self.df is None:
            return
    
        column = self.combo1.currentText()
    
        box_plot(self.df, column)
    
        self.output.setText(
            f"Box plot created successfully.\n\n"
            f"Variable : {column}"
        )
        
    def run_regression_plot(self):

        if self.df is None:
            return
    
        x = self.combo1.currentText()
        y = self.combo2.currentText()
    
        if x == y:
            self.output.setText("Please select two different variables.")
            return
    
        regression_plot(self.df, x, y)
    
        self.output.setText(
            f"Regression plot created successfully.\n\n"
            f"X-axis : {x}\n"
            f"Y-axis : {y}"
        )
        
    def run_qq_plot(self):

        if self.df is None:
            return
    
        column = self.combo1.currentText()
    
        qq_plot(self.df, column)
    
        self.output.setText(
            f"QQ Plot created successfully.\n\n"
            f"Variable : {column}"
        )
        
    def run_bland_altman(self):

        if self.df is None:
            return
    
        x = self.combo1.currentText()
        y = self.combo2.currentText()
    
        if x == y:
            self.output.setText("Please select two different variables.")
            return
    
        bland_altman_plot(self.df, x, y)
    
        self.output.setText(
            f"Bland-Altman Plot created successfully.\n\n"
            f"Variable 1 : {x}\n"
            f"Variable 2 : {y}"
        )
    
    def export_results(self):

        if self.current_result is None:
            self.output.setText("No analysis results available.")
            return
    
        filename, _ = QFileDialog.getSaveFileName(
            self,
            "Save Results",
            "Results.xlsx",
            "Excel Files (*.xlsx)"
        )
    
        if not filename:
            return
    
        try:
    
            if hasattr(self.current_result, "to_excel"):
                export_dataframe(self.current_result, filename)
                self.output.append(f"\n\nResults exported successfully:\n{filename}")
    
            else:
                self.output.append(
                    "\n\nExport currently supports descriptive statistics only."
                )
    
        except Exception as e:
            self.output.append(f"\n\nExport failed:\n{e}")
            self.statusBar().showMessage("Results exported successfully")
            
    def show_about(self):

            QMessageBox.about(
                self,
                "About AJ Research Toolkit",
                """
        <h2>AJ Research Toolkit</h2>
        
        <b>Version:</b> 1.0.0 <br>
        
        <b>Developer:</b> Ajithkumar M <br>
        
        <b>Institute:</b><br>
        Department of Medical Physics<br>
        National Cancer Institute (NCI)<br>
        All India Institute of Medical Sciences (AIIMS), Jhajjar, Haryana, India <br>
        
        <b>Description:</b><br>
        Statistical and Graphical Analysis Software
        for Biomedical and Medical Physics Research. <br>
        
        <b>Features</b><br>
        
        • Descriptive Statistics
        
        • Paired & Independent Tests
        
        • Correlation
        
        • Linear Regression
        
        • Publication-quality Graphs
        
        • Excel / CSV Export
        
        • High-resolution Image Export <br>
        
              © 2026 Ajithkumar M
        """
            )
        
    def export_csv_file(self):

        if self.current_result is None:
            self.output.setText("No results available.")
            return
    
        filename, _ = QFileDialog.getSaveFileName(
            self,
            "Save CSV",
            "Results.csv",
            "CSV Files (*.csv)"
        )
    
        if not filename:
            return
    
        try:
            if hasattr(self.current_result, "to_csv"):
                export_csv(self.current_result, filename)
                self.output.append(f"\n\nCSV exported:\n{filename}")
            else:
                self.output.append("\nCurrent result cannot be exported to CSV.")
    
        except Exception as e:
            self.output.append(str(e))
            
            
    def save_graph(self):

        from modules import graphs
    
        if graphs.CURRENT_FIGURE is None:
            self.output.setText("No graph available.")
            return
    
        filename, _ = QFileDialog.getSaveFileName(
            self,
            "Save Graph",
            "Figure",
            "JPEG (*.jpg);;PNG (*.png);;TIFF (*.tiff);;PDF (*.pdf);;SVG (*.svg)"
        )
    
        if filename:
            graphs.CURRENT_FIGURE.savefig(
                filename,
                dpi=600,
                bbox_inches="tight"
            )
    
            self.output.append(f"\n\nGraph saved successfully:\n{filename}")
            self.statusBar().showMessage("Graph saved successfully")
            
            
            
            
            