package com.example.marinesoftapplication

import android.content.ClipData
import android.content.Intent
import android.graphics.drawable.Drawable
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.MenuItem
import android.view.View
import android.widget.*
import androidx.drawerlayout.widget.DrawerLayout
import com.google.android.material.bottomnavigation.BottomNavigationView
import com.google.android.material.floatingactionbutton.FloatingActionButton
import com.google.android.material.navigation.NavigationBarItemView
import com.google.android.material.navigation.NavigationView
import com.google.firebase.auth.FirebaseAuth
import com.google.firebase.auth.ktx.auth
import com.google.firebase.ktx.Firebase

class DataActivity : AppCompatActivity() {

    lateinit var speciesName:TextView
    lateinit var quantity:TextView
    lateinit var time:TextView
    lateinit var speciesImage:ImageView

    private lateinit var auth : FirebaseAuth
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_data)

        auth = Firebase.auth

        val addedRow=findViewById<TableRow>(R.id.addedRow)
        quantity=findViewById(R.id.quantityText1)
        time=findViewById(R.id.timeText1)

        val name=intent.getStringExtra(EXTRA_MESSAGE)
        addedRow.visibility=View.GONE

        speciesName=findViewById<TextView?>(R.id.speciesTextadd).apply {
            text= name
            if(text!= null) {
                addedRow.visibility = View.VISIBLE
            }else{
                addedRow.visibility=View.GONE
            }
        }

        speciesImage=findViewById(R.id.speciesImage1)

//        navigation

        val signOut=findViewById<NavigationBarItemView>(R.id.signOut)
        val graph=findViewById<NavigationBarItemView>(R.id.graph)
        val analytic=findViewById<NavigationBarItemView>(R.id.analytic)
        val home=findViewById<NavigationBarItemView>(R.id.home_menu)
        val uploadButton=findViewById<NavigationBarItemView>(R.id.imageUpload)

        graph.setOnClickListener {
            startActivity(Intent(this,GraphActivity::class.java))
        }

        analytic.setOnClickListener {
            startActivity(Intent(this, AnalyticActivity::class.java))
        }
        // Authentiation
        signOut.setOnClickListener{
            Firebase.auth.signOut()
            updateUI()
        }
        uploadButton.setOnClickListener {
            val intent=Intent(this,UploadActivity::class.java)
            startActivity(intent)
        }


    }



    private fun updateUI() {
        val intent= Intent(this,SignInPage::class.java)
        startActivity(intent)
        finish()
    }
}